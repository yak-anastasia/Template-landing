from django import forms
from captcha.fields import CaptchaField
import datetime
class MyForm(forms.Form):
    name = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Имя', 'id':'sendemailname'}))
    email = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Email', 'type':'email', 'id':'sendemailemail'}))
    message = forms.CharField(label="", widget=forms.Textarea(attrs={'class':'form-control', 'placeholder':'Сообщение', 'rows':'3', 'id':'sendemailmessage'}))
    captcha = CaptchaField()

SERVICE_CHOICES =(
    (0, "xxxxxxxxxxxxxxxxxxxxxxxxxxxx"),
    (1, "xxxxxxxxxxxxxxxxxxxxxxxx"),
    (2, "xxxxxxxxxxxxxxxxxx"),
    (3, "xxxxxxxxxxxxxxxxx"),
    (4, "xxxxxxxxxxxxxxxxxxx"),
    (5, "xxxxxxxxxxxxx"),
    (6, "xxxxxx"),
)
number_errors = {
    'required': 'Укажите номер в формате: +79876543210.',
    'invalid': 'Номер должен быть в формате: +79876543210.'
}
service_errors = {
    'required': 'Выберите хотя бы одну услугу.',
    'invalid': 'Выберите хотя бы одну услугу.'
}
class OrderForm(forms.Form):
    name = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Имя'}))
    surname = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Фамилия'}))
    service = forms.MultipleChoiceField( required=True, choices=SERVICE_CHOICES, widget=forms.CheckboxSelectMultiple(), error_messages=service_errors)
    datetime = forms.DateTimeField(initial=datetime.date.today, widget=forms.DateTimeInput(attrs={'type':'datetime-local', 'class':'form-control', 'placeholder':'form-control'}) )
    phone = forms.RegexField(regex=r'^\+?1?\d{9,15}$', error_messages=number_errors, widget=forms.TextInput(attrs={'class':'form-control', 'type':'tel', 'placeholder':'+79876543210'}))
    comment = forms.CharField(label="", required=False, widget=forms.Textarea(attrs={'class':'form-control', 'placeholder':'Комментарий', 'rows':'5'}))
    captcha = CaptchaField()