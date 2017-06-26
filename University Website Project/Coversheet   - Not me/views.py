import mimetypes

from django.http import HttpResponse
from py2docx.docx import Docx #Importing py2docx library to generate coversheet
from py2docx.elements import Block
from py2docx.elements.text import InlineText, Break
from py2docx.elements.table import Table, Cell
import sqlite3
from .forms import NameForm
from django.shortcuts import render
from django.views.static import serve
import os
import sys

try:
    sys.path.insert(0, '../Mysite/')
    from CourseWorkDetails import CourseworkDetail
except:
    sys.path.insert(0, './Mysite/')
    from CourseWorkDetails import CourseworkDetail



################THE FORMS IMPORT LINE IS COMMENTED#######################


def create_docx(studentName, studentID, moduleCode, sqlDB):
    # Defining cursor for the database
    cur = sqlDB.cursor()
    # Defining SQL to pull dataset from Database
    cur.execute('SELECT * FROM ModuleInfoTable WHERE Module_Code = ?', (moduleCode, ))
    print cur.arraysize
    # Iterating through CourseworkDetail dataset INTEGRATED WITH ROWAN and assigning data to cw1
    for row in cur:
        cw1 = CourseworkDetail(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8])
    # Initialising py2docx variable
    doc = Docx()
    # Assigning newly entered details from web UI INTEGRATED WITH ROWAN
    cw1.assignStudentDetails(studentID, studentName)
    # Generating fields within docx file that's being built
    title = InlineText("Cover Sheet", bold=True, uppercase=True, size=20)
    mCode = InlineText("Module Code: " + cw1.moduleCode)
    mTitle = InlineText("Module Title: " + cw1.moduleTitle)
    mTutor = InlineText("Module Tutor: " + cw1.moduleTutor)
    cwNumber = InlineText("Coursework Number: " + str(cw1.cwNumber))
    cwTitle = InlineText("Coursework Title: " + cw1.cwTitle)
    iDate = InlineText("Issue Date: " + cw1.dateIssued)
    dDate = InlineText("Due Date and Time: " + cw1.dateDue)
    aType = InlineText("Assessment Type: " + cw1.assessType)
    pMark = InlineText("Percentage of Module Mark: " + str(cw1.moduleMark))
    sId = InlineText("Student ID: " + str(cw1.studentID))
    sName = InlineText("Student Name: " + cw1.studentName)

    # Assigning new block for each generated field above, to ensure clear spacing and readability
    b0 = Block(align='center')
    b1 = Block()
    b2 = Block()
    b3 = Block()
    b4 = Block()
    b5 = Block()
    b6 = Block()
    b7 = Block()
    b8 = Block()
    b9 = Block()
    b10 = Block()
    b11 = Block()

    # Adding each variable into it's respective block
    b0.append(title)
    b1.append(mCode)
    b2.append(mTitle)
    b3.append(mTutor)
    b4.append(cwNumber)
    b5.append(cwTitle)
    b6.append(iDate)
    b7.append(dDate)
    b8.append(aType)
    b9.append(pMark)
    b10.append(sId)
    b11.append(sName)

    # Adding tables, one for the 'coversheet' title, another for values entered by the tutor/student
    t0 = Table(width="80%", padding='2cm', border={'left': {'color': '#000000', 'size': '4pt', 'style': 'solid'},
                                                   'bottom': {'color': '#000000', 'size': '4pt', ' style': 'solid'},
                                                   'top': {'color': '#000000', 'size': '4pt', 'style': 'solid'},
                                                   'right': {'color': '#000000', 'size': '4pt', 'style': 'solid'}})

    t1 = Table(width="80%", padding='2cm', border={'left': {'color': '#000000', 'size': '2pt', 'style': 'solid'},
                                    'bottom': {'color': '#000000', 'size': '2pt', ' style': 'solid'},
                                    'top': {'color': '#000000', 'size': '2pt', 'style': 'solid'},
                                    'right': {'color': '#000000', 'size': '2pt', 'style': 'solid'}})
    # Appending all blocks to their respective cells so they can be appended to the doc variable created earlier
    c0 = Cell()
    c1 = Cell()
    c0.append(b0)
    c1.append(b1)
    c1.append(b2)
    c1.append(b3)
    c1.append(b4)
    c1.append(b5)
    c1.append(b6)
    c1.append(b7)
    c1.append(b8)
    c1.append(b9)
    c1.append(b10)
    c1.append(b11)

    # Adding each table to it's respective row, (coversheet as title in first row, then values entered by student/tutor below
    t0.add_row([c0])
    t1.add_row([c1])

    # Appending tables to the doc variable with a brake tag in between (So adequate spacing is used for readability
    doc.append(t0)
    doc.append(Block(Break()))
    doc.append(t1)

    # Saving the file with a custom name (student name + student ID + module code + Coversheet.docx)
    filename = "./" + cw1.studentName + '_' + str(cw1.studentID) + '_' + cw1.moduleCode + "_Coversheet.docx"
    doc.save(filename)
    return os.path.abspath(filename)


def postnew(request):

    # Initialising variables to store details entered from student
    Student_Name = "No data entry"
    Student_ID = "No data entry"
    Module_Code = "No data entry"

    if request.method == "POST":
        # Retrieve the posted form from the student
        MyNameForm = NameForm(request.POST)
        print "post"
        if MyNameForm.is_valid():

            # Cleaning the data entered by the student
            print "valid form"
            Student_Name = MyNameForm.cleaned_data['Student_Name']
            Student_ID = MyNameForm.cleaned_data['Student_ID']
            Module_Code = MyNameForm.cleaned_data['Module_Code']

            # Initliasing database connection to pull tutor entered details
            conn = sqlite3.connect('ModuleInfoDB.sqlite3')

            # Calling the function to create docx details from database and freshly entered details from student
            filepath = create_docx(Student_Name, Student_ID, Module_Code, conn)
            print "serving"

            # Serving the file to the user through an automatic download once form is submitted
            new_serve_request = serve(request, os.path.basename(filepath), os.path.dirname(filepath))
            new_serve_request['Content-Disposition'] = "attachment; filename={0}".format(Student_Name + '_' + Student_ID + '_' + Module_Code + ".docx")
            return new_serve_request
        else:
            MyNameForm = NameForm

    # Rendering the post_edit.html page until a POST is seen
    text_file = open("Output.txt", "w")
    text_file.write("Purchase Amount: %s" % Student_Name + Student_ID + Module_Code)
    text_file.close()
    return render(request, 'Coversheet/post_edit.html')

'''
Student_Name = "george"
Student_ID = "12345"
Module_Code = "340ct"
conn = sqlite3.connect('ModuleInfoDB.sqlite3') # Maybe doesn't need dots?
create_docx(Student_Name, Student_ID, Module_Code, conn)
'''

