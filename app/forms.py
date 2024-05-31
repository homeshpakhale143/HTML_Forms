from django import forms
from app.models import *
from django.core.validators import MinLengthValidator, MaxLengthValidator, RegexValidator
def starts_with_a(value):
    if value[0] in ['a','A']:
        raise forms.ValidationError('name not starts with a')
    
def len_is_4(value):
    if len(value)<=4:
        raise forms.ValidationError('Length is must be greater than 4')

class TopicForm(forms.Form):
    tn=forms.CharField(validators=[starts_with_a,len_is_4])
    mobno=forms.CharField(min_length=10,max_length=10,validators=[RegexValidator('[6-9]\d{9}')])

class WebpPageForm(forms.Form):
    tn=forms.ModelChoiceField(queryset=Topic.objects.all())
    name=forms.CharField(validators=[starts_with_a,])
    url=forms.URLField()
    email=forms.EmailField()
    reemail=forms.EmailField()
    # bootcatcher=forms.CharField()


    def clean_bootcatcher(self):
        bootcatcher=self.cleaned_data['bootcatcher']
        if len(bootcatcher)>0:
            raise forms.ValidationError('Automated software not possible')
        
    def clean(self):
        e=self.cleaned_data['email']
        re=self.cleaned_data['reemail']
        if e!=re:
            raise forms.ValidationError('Email not matched')        

    def clean_url(self):
        u=self.cleaned_data['url']
        if u[-1]=='n':
            raise forms.ValidationError('Not ended with .in')


class AccessRecord(forms.Form):
    tn=forms.ModelChoiceField(queryset=Webpage.objects.all())
    name=forms.CharField(max_length=100)
    author=forms.CharField(max_length=100)
    date=forms.DateField()

