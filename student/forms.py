from django import forms
from . import models
# create a ModelForm
class StudentForm(forms.ModelForm):
    # specify the name of model to use 
    class Meta:
        model = models.Student
        fields = "__all__"
    # this function will be used for the validation 
    def clean(self):
        # data from the form is fetched using super function 
        super(StudentForm, self).clean()
        # extract the username and text field from the data 
        f_name  =self.cleaned_data.get('f_name')
        l_name =self.cleaned_data.get('l_name')
        mobile =self.cleaned_data.get('mobile')
        birth_date =self.cleaned_data.get('birth_date')
        
        # validate data 
        # conditions to be met for the username length 
        if len(f_name) < 2:
            self._errors['f_name'] = self.error_class([ 'Minimum 2 characters required'])
        if len(l_name) < 2:
            self._errors['l_name'] = self.error_class(['Minimum 2 characters required'])
        if len(str(mobile)) < 10:
            self._errors['mobile'] = self.error_class(['Minimum mobile 10 characters required'])   
            
        # return any errors if found 
        return self.cleaned_data