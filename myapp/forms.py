from django import forms
from django.core import validators

class StudentForm(forms.Form):
    name=forms.CharField(max_length=30)
    age=forms.IntegerField()

    def clean_name(self):
        inputname=self.cleaned_data['name']
        if not(inputname.isalpha()):
            raise ValueError("Value should be String")
        return inputname
    def clean_age(self):
        inputage=self.cleaned_data['age']
        if inputage<0:
            raise ValueError("Age should not be negative")
        return inputage

class StudentForm2(forms.Form):
    name=forms.CharField(max_length=30,validators=[validators.MaxLengthValidator(5)])
    age=forms.IntegerField(validators=[validators.MinValueValidator(0),validators.MaxValueValidator(15)])
    


