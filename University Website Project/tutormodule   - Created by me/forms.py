from django import forms


class NameForm(forms.Form):
    # Each of the Module fields.
    Module_Code = forms.CharField(label='Module_Code', max_length=100)
    Module_Title = forms.CharField(label='Module_Title', max_length=100)
    Module_Tutor = forms.CharField(label='Module_Tutor', max_length=100)
    Cw_No = forms.CharField(label='Cw_No', max_length=100)
    Cw_Title = forms.CharField(label='Cw_Title', max_length=100)
    Issue_Date = forms.CharField(label='Issue_Date', max_length=100)
    Due_Date_Time = forms.CharField(label='Due_Date_Time', max_length=100)
    Assessment_Type = forms.CharField(label='Assessment_Type', max_length=100)
    Percentage_Of_Module = forms.CharField(label='Percentage_Of_Module', max_length=100)
