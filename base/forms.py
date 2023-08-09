from django.forms import ModelForm, TextInput, EmailInput, Textarea
from .models import Contact

class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ['full_name','email','message']

        labels = {
            'full_name':'',
            'email':'',
            'message':''
        }

        widgets = {
            'full_name': TextInput(attrs={'name':"name", 'id':"name" ,'type':"text", 'class':"form-control", 'placeholder':"Your Name"}),
            'email': EmailInput(attrs={'name':"email", 'id':"email", 'type':"email", 'class':"form-control", 'placeholder':"Email"}),
            'message': Textarea(attrs={'name':"comments", 'id':"comments", 'rows':"4", 'class':"form-control", 'placeholder':"Your Message"}),
        }