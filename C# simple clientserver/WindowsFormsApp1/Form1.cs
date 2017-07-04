using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.IO;
using System.Linq;
using System.Net.Sockets;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using doorclass;
using System.Runtime.Serialization.Formatters.Binary;
using System.Threading;

namespace WindowsFormsApp1
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void textBox1_TextChanged(object sender, EventArgs e)
        {

        }

        private void id_box_TextChanged(object sender, EventArgs e)
        {

        }

        private void checkBox1_CheckedChanged(object sender, EventArgs e)
        {

        }

        private void button1_Click(object sender, EventArgs e)
        // Add new door button, uses checkbox1 and textbox1
        {
            Console.WriteLine("button click.");

            TcpClient tcpclnt = new TcpClient();
            tcpclnt.Connect("192.168.0.11", 8888);
            Stream stm = tcpclnt.GetStream();
            Console.WriteLine("Connected.");
            ASCIIEncoding asen = new ASCIIEncoding();


            string id = (String.IsNullOrEmpty(id_box.Text)) ? "-1" : id_box.Text;
            bool check = (form_checkbox.Checked) ? true : false;
            string str = id + ',' + form_label.Text + ',' + check;
            byte[] ba = asen.GetBytes(str);

            stm.Write(ba, 0, ba.Length);
            stm.Close();
        }

        public void Main()
        {
            Console.WriteLine("Main");
            TcpClient tcpclnt = new TcpClient();
            tcpclnt.Connect("192.168.0.11", 8888);
            Stream stm = tcpclnt.GetStream();
            var bin = new BinaryFormatter();
            List<door> list = (List<door>)bin.Deserialize(stm);
            Console.WriteLine("Main finished.");


            /*
            ASCIIEncoding asen = new ASCIIEncoding();
            byte[] ba = asen.GetBytes(str);
            Console.WriteLine("Transmitting.....");

            stm.Write(ba, 0, ba.Length);

            byte[] bb = new byte[100];
            int k = stm.Read(bb, 0, 100);
            for (int i = 0; i < k; i++)
                Console.Write(Convert.ToChar(bb[i]));


            var bin = new BinaryFormatter();
            List<door> list = (List<door>)bin.Deserialize(stm);

            foreach (door d in list)
            {
                Console.Write("{0}, {1}, {2}\n", d.Id, d.Status, d.Label);
            }

            tcpclnt.Close();
            Console.ReadKey();
            */
        }

        
        private void dataGridView1_CellContentClick(object sender, DataGridViewCellEventArgs e)
        {

        }

        private void timer1_Tick(object sender, EventArgs e)
        {
            try
            {
                TcpClient tcpclnt = new TcpClient();
                tcpclnt.Connect("192.168.0.11", 8888);
                Stream stm = tcpclnt.GetStream();
                Console.WriteLine("Connected.");

                ASCIIEncoding asen = new ASCIIEncoding();

                byte[] ba = asen.GetBytes("update");
                Console.WriteLine(ba);
                stm.Write(ba, 0, ba.Length);

                var bin = new BinaryFormatter();
                List<door> list = (List<door>)bin.Deserialize(stm);

                dataGridView1.Rows.Clear();

                foreach (door d in list)
                {
                    dataGridView1.Rows.Add(d.Id, d.Status, d.Label);
                }

                dataGridView1.Update();
                dataGridView1.Refresh();
            }
            catch
            {

            }
        }
    }
}
