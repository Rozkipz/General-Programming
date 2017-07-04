using System;
using System.Collections.Generic;
using System.Data.SqlClient;
using System.Net;
using System.Net.Sockets;
using System.Runtime.Serialization.Formatters.Binary;
using doorclass;
using System.Text.RegularExpressions;
using System.Text;

namespace DoorsApp
{
        class Program
    {
        static List<door> get_doors(SqlConnection sqlcon)
        {
            List<door> doors = new List<door>();
            using (SqlCommand select_ids = new SqlCommand("SELECT * FROM doors", sqlcon))
            {
                SqlDataReader reader = select_ids.ExecuteReader();
                while (reader.Read())
                {
                    int id = reader.GetInt32(0);
                    string label = reader.GetString(1);
                    bool status = reader.GetBoolean(2);
                    doors.Add(new door() { Id = id, Label = label, Status = status });
                }
            }
            return doors;
        }

        static void create_db(SqlConnection sqlcon)
        {
            try
            {
                var create_db_command = sqlcon.CreateCommand();
                create_db_command.CommandText = "CREATE DATABASE doors_db";
                create_db_command.ExecuteNonQuery();
                Console.WriteLine("DB created.\n");
            }
            catch (SqlException e)
            {
                Console.WriteLine(e.Message);
                Console.Write("Db already made.\n");
            }
            catch (Exception e)
            {
                Console.WriteLine("An error occured");
                Console.WriteLine(e.Message);
                Console.ReadKey();
                Environment.Exit(1);

            }
        }

        static void insert_into_table(SqlConnection sqlcon, string label, bool status)
        {
            using (SqlCommand command = new SqlCommand("INSERT INTO doors(label, status) VALUES(@label, @status)", sqlcon))
            {
                command.Parameters.Add(new SqlParameter("label", label));
                command.Parameters.Add(new SqlParameter("status", status));
                command.ExecuteNonQuery();
            }
        }

        static void update_table(SqlConnection sqlcon, int id, string label, bool status)
        {
            using (SqlCommand command = new SqlCommand("UPDATE doors SET label=@label, status=@status WHERE id=@id", sqlcon))
            {
                command.Parameters.Add(new SqlParameter("id", id));
                command.Parameters.Add(new SqlParameter("label", label));
                command.Parameters.Add(new SqlParameter("status", status));
                command.ExecuteNonQuery();
            }
        }

        static void create_table(SqlConnection sqlcon)
        {
            try
            {
                System.Data.DataTable dt = sqlcon.GetSchema("Tables");
                List<string> tables_schema = new List<string>();
                foreach (System.Data.DataRow row in dt.Rows)
                {
                    tables_schema.Add(Convert.ToString(row[2]));
                }
                if (!tables_schema.Contains("doors"))
                {
                    Console.WriteLine("Doesn't contain doors");
                    using (SqlCommand create_doors_table = new SqlCommand("CREATE TABLE doors (id INT PRIMARY KEY IDENTITY(1,1), label TEXT, status BIT)", sqlcon))
                    {
                        var t = create_doors_table.ExecuteNonQuery();
                        Console.WriteLine(t);
                        Console.WriteLine("Table made");
                    }
                }
            }
            catch (Exception e)
            {
                Console.WriteLine("An error occured");
                Console.WriteLine(e.ToString());
                Console.ReadKey();
                Environment.Exit(1);
            }
        }

        static void Main(string[] args)
        {
            //; Integrated Security = True
            SqlConnection sqlCon = new SqlConnection("Data Source = (LocalDB)\\MSSQLLocalDB");
            sqlCon.Open();
            create_db(sqlCon);
            sqlCon.Close();
            
            //Log in with DB specified.
            sqlCon = new SqlConnection("Data Source = (LocalDB)\\MSSQLLocalDB;database=doors_db;MultipleActiveResultSets=true");
            sqlCon.Open();
            create_table(sqlCon);
            sqlCon.Close();

            //insert_into_table(sqlCon, "THIS IS A LABEL", true);
            
            TcpListener serverSocket = new TcpListener(IPAddress.Parse("192.168.0.11"), 8888);
            serverSocket.Start();

            while (true)
            {
                Console.WriteLine("Waiting for a connection.....");
                Socket s = serverSocket.AcceptSocket();
                Console.WriteLine("Connection accepted from " + s.RemoteEndPoint);
                /*
                int k = s.Receive(b);
                Console.WriteLine(k);
                */

                System.IO.Stream stream = new NetworkStream(s);
                var bin = new BinaryFormatter();

                byte[] b = new byte[100];
                int k = s.Receive(b);
                string sent_str = Encoding.ASCII.GetString(b, 0, k);
                
                if (sent_str == "update")
                {
                    sqlCon = new SqlConnection("Data Source = (LocalDB)\\MSSQLLocalDB;database=doors_db;MultipleActiveResultSets=true");
                    sqlCon.Open();
                    var all_doors = get_doors(sqlCon);
                    bin.AssemblyFormat = System.Runtime.Serialization.Formatters.FormatterAssemblyStyle.Simple;
                    bin.Serialize(stream, all_doors);
                    Console.WriteLine("\nSent Acknowledgement");

                    s.Close();
                    sqlCon.Close();
                }

                else
                {
                    sqlCon = new SqlConnection("Data Source = (LocalDB)\\MSSQLLocalDB;database=doors_db;MultipleActiveResultSets=true");
                    sqlCon.Open();
                    Console.WriteLine(sent_str);
                    string[] values = sent_str.Split(',');
                    
                    Console.WriteLine(values[0]); //id
                    Console.WriteLine(values[1]); //label
                    Console.WriteLine(values[2]); //checked 0=false 1=true

                    if (Convert.ToInt16(values[0]) != -1)
                    {
                        update_table(sqlCon, Convert.ToInt16(values[0]), values[1], Convert.ToBoolean(values[2]));
                    }

                    insert_into_table(sqlCon, values[1], Convert.ToBoolean(values[2]));

                    s.Close();
                    sqlCon.Close();
                }
                
            }
        }
    }
}
