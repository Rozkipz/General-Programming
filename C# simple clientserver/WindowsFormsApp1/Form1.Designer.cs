namespace WindowsFormsApp1
{
    partial class Form1
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            this.components = new System.ComponentModel.Container();
            this.button1 = new System.Windows.Forms.Button();
            this.form_label = new System.Windows.Forms.TextBox();
            this.form_checkbox = new System.Windows.Forms.CheckBox();
            this.dataGridView1 = new System.Windows.Forms.DataGridView();
            this.timer1 = new System.Windows.Forms.Timer(this.components);
            this.id = new System.Windows.Forms.DataGridViewTextBoxColumn();
            this.Status = new System.Windows.Forms.DataGridViewTextBoxColumn();
            this.Label = new System.Windows.Forms.DataGridViewTextBoxColumn();
            ((System.ComponentModel.ISupportInitialize)(this.dataGridView1)).BeginInit();
            this.SuspendLayout();
            // 
            // button1
            // 
            this.button1.Location = new System.Drawing.Point(485, 315);
            this.button1.Name = "button1";
            this.button1.Size = new System.Drawing.Size(102, 40);
            this.button1.TabIndex = 0;
            this.button1.Text = "New door";
            this.button1.UseVisualStyleBackColor = true;
            this.button1.Click += new System.EventHandler(this.button1_Click);
            // 
            // form_label
            // 
            this.form_label.Location = new System.Drawing.Point(485, 266);
            this.form_label.Name = "form_label";
            this.form_label.Size = new System.Drawing.Size(102, 20);
            this.form_label.TabIndex = 1;
            this.form_label.Text = "Enter Label";
            this.form_label.TextChanged += new System.EventHandler(this.textBox1_TextChanged);
            // 
            // form_checkbox
            // 
            this.form_checkbox.AutoSize = true;
            this.form_checkbox.Location = new System.Drawing.Point(512, 292);
            this.form_checkbox.Name = "form_checkbox";
            this.form_checkbox.Size = new System.Drawing.Size(46, 17);
            this.form_checkbox.TabIndex = 2;
            this.form_checkbox.Text = "On?";
            this.form_checkbox.UseVisualStyleBackColor = true;
            this.form_checkbox.CheckedChanged += new System.EventHandler(this.checkBox1_CheckedChanged);
            // 
            // dataGridView1
            // 
            this.dataGridView1.ColumnHeadersHeightSizeMode = System.Windows.Forms.DataGridViewColumnHeadersHeightSizeMode.AutoSize;
            this.dataGridView1.Columns.AddRange(new System.Windows.Forms.DataGridViewColumn[] {
            this.id,
            this.Status,
            this.Label});
            this.dataGridView1.Location = new System.Drawing.Point(12, 12);
            this.dataGridView1.Name = "dataGridView1";
            this.dataGridView1.Size = new System.Drawing.Size(433, 702);
            this.dataGridView1.TabIndex = 3;
            this.dataGridView1.CellContentClick += new System.Windows.Forms.DataGridViewCellEventHandler(this.dataGridView1_CellContentClick);
            // 
            // timer1
            // 
            this.timer1.Enabled = true;
            this.timer1.Interval = 1000;
            this.timer1.Tick += new System.EventHandler(this.timer1_Tick);
            // 
            // id
            // 
            this.id.HeaderText = "Door ID";
            this.id.Name = "id";
            this.id.ReadOnly = true;
            // 
            // Status
            // 
            this.Status.HeaderText = "Door status";
            this.Status.Name = "Status";
            this.Status.ReadOnly = true;
            // 
            // Label
            // 
            this.Label.HeaderText = "Label";
            this.Label.Name = "Label";
            this.Label.ReadOnly = true;
            this.Label.Width = 150;
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(639, 721);
            this.Controls.Add(this.dataGridView1);
            this.Controls.Add(this.form_checkbox);
            this.Controls.Add(this.form_label);
            this.Controls.Add(this.button1);
            this.Name = "Form1";
            this.Text = "Form1";
            ((System.ComponentModel.ISupportInitialize)(this.dataGridView1)).EndInit();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Button button1;
        private System.Windows.Forms.TextBox form_label;
        private System.Windows.Forms.CheckBox form_checkbox;
        private System.Windows.Forms.DataGridView dataGridView1;
        private System.Windows.Forms.Timer timer1;
        private System.Windows.Forms.DataGridViewTextBoxColumn id;
        private System.Windows.Forms.DataGridViewTextBoxColumn Status;
        private System.Windows.Forms.DataGridViewTextBoxColumn Label;
    }
}

