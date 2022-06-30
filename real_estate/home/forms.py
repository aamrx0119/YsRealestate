from django import forms
from . import models



class ContactUSForm (forms.ModelForm) :
    class Meta :
        model = models.ContactUS
        fields = '__all__'

        labels = {
            "name": "",
            "email": "",
            "information": "",
            'subject':'',
            'pm':''
            
        }

        widgets = {

            'name':forms.TextInput(attrs={'class':'form-control name-contact','placeholder':'Your Name',}),
            'email':forms.EmailInput(attrs={'class':'form-control','placeholder':'Email',}),
            'subject':forms.TextInput(attrs={'class':'form-control','placeholder':'Subject',}),
            'pm':forms.Textarea(attrs={'class':'form-control','placeholder':'Message',}),
        }