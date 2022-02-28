from django import forms



class Sign_up (forms.Form):
    first_name = forms.CharField(max_length=50)