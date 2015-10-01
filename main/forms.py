from django import forms
from django.core.mail import send_mail


class ContactForm(forms.Form):
    name = forms.CharField(
        max_length=120
    )
    email = forms.EmailField()
    body = forms.CharField(
        widget=forms.Textarea
    )

    def send_email(self):
        send_mail(
            subject='Website contact',
            message=self['body'],
            from_email=self['email'],
            recipient_list=[
                'walters.justin01@gmail.com'
            ],
        )
