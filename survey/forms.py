import os
from django import forms
from .models import 


class InquiryForm(forms.Form):
    CHOICE = [
        ( 'アプリについて', 'アプリについて'),
        ( '商品について', '商品について'),
        ( 'その他について', 'その他について'),
    ]

    name = forms.CharField(label='お名前', max_length=30)
    email = forms.EmailField(label='メールアドレス')
    title = forms.ChoiceField(label='お問い合わせの種類', widget=forms.Select, choices= CHOICE, initial=0)
    message = forms.CharField(label='お問い合わせ内容', widget=forms.Textarea)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['name'].widget.attrs['class']='form-control'
        self.fields['name'].widget.attrs['placeholder']='山田 太郎'

        self.fields['email'].widget.attrs['class']='form-control'
        self.fields['email'].widget.attrs['placeholder']='xxx@email.com'

        self.fields['title'].widget.attrs['class']='form-control'

        self.fields['message'].widget.attrs['class']='form-control'
        self.fields['message'].widget.attrs['rows']='3'



class PersonalForm(forms.ModelForm):
    class Meta:
        model = Sample

        fields = ('gender', 'img')

        widgets = {
            'gender':forms.RadioSelect
        }
