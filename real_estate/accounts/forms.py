from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from home.models import House_model , Profile
from django.contrib.auth.forms import PasswordResetForm , PasswordChangeForm , SetPasswordForm

class Sign_up (forms.Form):
    username = forms.CharField(max_length=50,widget=forms.TextInput(attrs={'class':'form-control'}))
    first_name = forms.CharField(max_length=50 ,widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(max_length=50,widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.EmailField(max_length=50 ,widget=forms.EmailInput(attrs={'class':'form-control'}))
    password1 = forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'class':'form-control'}),max_length=65)
    password2 = forms.CharField(label='Confirm password',widget=forms.PasswordInput(attrs={'class':'form-control'}),max_length=65)


    def clean_email (self) :
        cd = self.cleaned_data
        user = User.objects.filter(email=cd['email'])
        if user.exists():
            raise forms.ValidationError('this email was used')
        return cd['email']
        


    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords don't match")
        return password2




class Log_in (forms.Form) :
    username = forms.CharField(label='Username or email ',max_length=50,widget=forms.TextInput(attrs={'class':'form-control p_input'}))  
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control p_input'}),max_length=65)

class House_Model_Form (forms.ModelForm):
    class Meta :
        model = House_model
        fields = ('name','compony','information')

        labels = {
            "name": "Name ",
            "compony": "Compony ",
            "information": "Detail ",
        }
        widgets = {

            'name': forms.TextInput(attrs={'class':'form-control',}),
            'information': forms.Textarea(attrs={'class':'form-control'}),
            'compony': forms.TextInput(attrs={'class':'form-control'}),
            # 'picture1': forms.FileInput(attrs={"name":"img[]","class":"file-upload-default"}),
        }
class Change_Profile (forms.ModelForm):
    class Meta :
        model = Profile
        fields = ('first_name','last_name',)

        labels = {
            "first_name": "Name ",
            "last_name": "Lastname ",
            # "picture": "Your picture ",
        }
        widgets = {

            'first_name': forms.TextInput(attrs={'class':'form-control',}),
            'last_name': forms.TextInput(attrs={'class':'form-control'}),
            # 'picture': forms.TextInput(attrs={'class':'form-control'}),
            # 'picture1': forms.FileInput(attrs={"name":"img[]","class":"file-upload-default"}),
        }



class Email_Forget_Form (PasswordResetForm) :

    email = forms.EmailField(label='Email',max_length=100,widget=forms.EmailInput(attrs={'class':'form-control',}))



    def clean_email (self) :
        Forget_email = self.cleaned_data.get('email')
        user = User.objects.filter(email=Forget_email)
        if not user.exists():
            raise ValidationError('oops your email is wrong')
        return Forget_email
        
class Email_Changepassword_Form (SetPasswordForm) :

    new_password1 = forms.CharField(label='New password',max_length=100,widget=forms.PasswordInput(attrs={'class':'form-control',}))
    new_password2 = forms.CharField(label='Confirm password',max_length=100,widget=forms.PasswordInput(attrs={'class':'form-control',}))



    def clean_new_password2 (self) :
        p2 = self.cleaned_data.get('new_password2')
        p1 = self.cleaned_data.get('new_password1')
        if p1 and p2 and p2 != p1 :
            raise ValidationError('Passwords arent same')
        return p2
        