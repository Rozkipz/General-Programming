from django import forms


from django import forms

# Defining student entered variables into the database

class NameForm(forms.Form):
    Student_Name = forms.CharField(label='Student_Name', max_length=100)
    Student_ID = forms.CharField(label='Student_ID', max_length=100)
    Module_Code = forms.CharField(label='Module_Code', max_length=100)

    # module code, module title, module tutor responsible for cw, cw no, cw title
    # issue date, due date and time, assessment type (individual/group)
    # % of module mark