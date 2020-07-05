from django import forms
from django.core import validators

class Myform(forms.Form):
    '''用户表单'''
    username = forms.CharField(max_length=255,min_length=2)
    password = forms.CharField(max_length=255,min_length=6)
    # yanzhen = forms.CharField(max_length=255)
    # email = forms.CharField(validators=[validators.EmailValidator(message="请输入正确的邮箱格式：")])
    # telephone = forms.CharField(validators=[validators.RegexValidator(r'1[3456789]\d{9}')])

class Mytlp(forms.Form):
    '''电话表单'''
    telephone = forms.CharField(validators=[validators.RegexValidator(r'1[3456789]\d{9}')])

class Mypwd(forms.Form):
    password = forms.PasswordInput()

class Modify(forms.Form):
    '''书籍信息修改表单'''
    logo = forms.ImageField()
    bname = forms.CharField(max_length=50,min_length=1)
    author = forms.CharField(min_length=1)
    fenlei = forms.CharField(min_length=1)
    details = forms.CharField(max_length=80)
