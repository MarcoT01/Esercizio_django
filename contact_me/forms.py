from django import forms


class ContactForm(forms.Form):
    email = forms.EmailField()
    subject = forms.CharField()
    msg_body = forms.CharField(widget=forms.Textarea)
