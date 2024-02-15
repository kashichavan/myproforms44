how to valid a field from forms by using clean_fieldName:
----------------------------------------------------------

class StudentForm(forms.Form):
    name=forms.CharField(max_length=30)
    age=forms.IntegerField()

Step1 ) create a method ie: clean_fieldName(self) inside the form class
		 def clean_name(self):

step2 ) get the form data into the method

		varname=self.cleaned_data['fieldname']
		
		ex:
		 inputname=self.cleaned_data['name']

step 3) apply python logic on the data for validation if validation is not correct than raise an 
	exception

	ex: i wanto check whether my given name contains non alpha characters
 		
	if not(inputname.isalpha()):
            raise ValueError("Value should be String")

Step 4) if validation is correct than return input data

	ex: 
		return inputname


validations by using inbuilt core validators:
------------------------------------------------

step 1) first import validators module from django.core


step 2) go to form class and choose the field


step 3) for the field give the arguement as validators=[val1,val2,...,valn]

class StudentForm2(forms.Form):
    name=forms.CharField(max_length=30,validators=[validators.MaxLengthValidator(5)])             
    age=forms.IntegerField(validators=[validators.MinValueValidator(0),validators.MaxValueValidator(15)])

step 4) go to views write else for for.is_valid() condition in that else block raise an exception


	if form.is_valid():
            name=form.cleaned_data['name']
            age=form.cleaned_data['age']
            StudentModel.objects.create(name=name,age=age)
        else:
             raise ValueError("Form is invalid")
    


















