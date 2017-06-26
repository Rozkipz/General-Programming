from .forms import NameForm
from django.shortcuts import render
import sqlite3


def complete(request):
    return render(request, 'tutormodule/complete.html')
    # This is returned when a successful form has been submitted.


def getmoduleinfo(request):
    module_code = "No data entry"
    module_title = "No data entry"
    module__tutor = "No data entry"
    cw__no = "No data entry"
    cw__title = "No data entry"
    issue__date = "No data entry"
    due__date__time = "No data entry"
    assessment__type = "No data entry"
    percentage__of__module = "No data entry"
    # Adds default values for all the entries needed to create a new module in the DB.

    data_entered = False
    # Adds a bool value that allows for a check if the data has been submitted by user.

    if request.method == "POST":
        module_info_form = NameForm(request.POST)
        # Creates a new form

        if module_info_form.is_valid():
            data_entered = True
            # Changes the bool variable to indicate data has been entered.

            module_code = module_info_form.cleaned_data['Module_Code']
            module_title = module_info_form.cleaned_data['Module_Title']
            module__tutor = module_info_form.cleaned_data['Module_Tutor']
            cw__no = module_info_form.cleaned_data['Cw_No']
            cw__title = module_info_form.cleaned_data['Cw_Title']
            issue__date = module_info_form.cleaned_data['Issue_Date']
            due__date__time = module_info_form.cleaned_data['Due_Date_Time']
            assessment__type = module_info_form.cleaned_data['Assessment_Type']
            percentage__of__module = module_info_form.cleaned_data['Percentage_Of_Module']
            # Assigns the values given by user to a variable inside the module_info_form

    if data_entered:
        # Checks if data has been entered.

        #############################################################################
        #   This is the stuff that is integrated with George.                       #
        #   The module input from the user is then used by him to generate a        #
        #   coversheet that is available for download.                              #
        #############################################################################

        sqldb = sqlite3.connect('ModuleInfoDB.sqlite3')
        cursor = sqldb.cursor()
        # Connects to SQL db.

        try:
            cursor.execute('SELECT * FROM ModuleInfoTable WHERE Module_Code = ?', (module_code,))
            # This runs an SQL command to select everything from the module code entered by the user.

            if cursor.arraysize > 0:
                # This checks if there is already a field with that module code.
                print "Deleted module code: ", module_code
                cursor.execute('DELETE from ModuleInfoTable where Module_Code=?', (module_code,))
                # This deletes that field.

            cursor.execute(
                'INSERT INTO ModuleInfoTable (Module_Code, Module_Title, Module_Tutor, Cw_No, Cw_Title, Issue_Date, Due_Date_Time, Assessment_Type, Percentage_Of_Module) VALUES ( ?, ?, ?, ?, ?, ?, ?, ?, ? )',
                (module_code, module_title, module__tutor, cw__no, cw__title, issue__date, due__date__time,
                 assessment__type, percentage__of__module))
            sqldb.commit()
            # This adds the new module to the database and commits it.

        except OperationalError:
            # This occurs when a table hasn't been created in the DB.

            cursor.execute(
                'CREATE TABLE ModuleInfoTable (Module_Code TEXT, Module_Title TEXT, Module_Tutor TEXT, Cw_No INTEGER, Cw_Title TEXT, Issue_Date DATE, Due_Date_Time DATE, Assessment_Type TEXT, Percentage_Of_Module INTEGER)')
            # Creates a new table.

            cursor.execute(
                'INSERT INTO ModuleInfoTable (Module_Code , Module_Title, Module_Tutor, Cw_No, Cw_Title, Issue_Date, Due_Date_Time, Assessment_Type, Percentage_Of_Module) VALUES ( ?, ?, ?, ?, ?, ?, ?, ?, ? )',
                (module_code, module_title, module__tutor, cw__no, cw__title, issue__date, due__date__time,
                 assessment__type, percentage__of__module))
            sqldb.commit()
            # Adds the new module to the DB.

        sqldb.close()
        # Closes the DB
        #############################################################################################################

        return render(request, 'tutormodule/complete.html')
        # Returns an all successful page.

    return render(request, 'tutormodule/base.html')
    # Returns the base html page with the form on.
