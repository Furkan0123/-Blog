from django import forms
from .models import ContactMessage

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'message']

    message = forms.CharField(widget=forms.Textarea(attrs={'rows': 4}))

