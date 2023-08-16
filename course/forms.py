from django import forms
from . import models
# create a ModelForm
class CourseForm(forms.ModelForm):
    # specify the name of model to use 
    class Meta:
        model = models.Course
        fields = "__all__"
    # this function will be used for the validation 
    def clean(self):
        # data from the form is fetched using super function 
        super(CourseForm, self).clean()
        # extract the username and text field from the data 
        title  =self.cleaned_data.get('title')
        description =self.cleaned_data.get('description')
     
        # validate data 
        # conditions to be met for the username length 
        if len(title) < 2:
            self._errors['title'] = self.error_class([ 'Minimum 2 characters required'])

        if len(description) < 10:
            self._errors['description'] = self.error_class(['Minimum  10 characters required'])   
            
        # return any errors if found 
        return self.cleaned_data