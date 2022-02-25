from django import forms
from django.core.exceptions import ValidationError

from b_app.models import Author, Publisher


def check_year(value):
    if value < -5000:
        raise ValidationError("NIe bylo książek w tym czasie")

class AddBookForm(forms.Form):
    title = forms.CharField()
    year = forms.IntegerField(validators=[check_year, ])
    author = forms.ModelChoiceField(queryset=Author.objects.all())

    def clean(self):
        data = super().clean()
        errors = []
        if data['title'][0].lower() == 'ś' and data['year']>-1500:
            errors.append('jakis babol')


class AddPublisherForm(forms.Form):
    name = forms.CharField()
    address = forms.CharField()


class AddPublisherModelForm(forms.ModelForm):

    class Meta:
        model = Publisher
        exclude = ['books']
        widgets = {
            'name':forms.PasswordInput(attrs={'placeholder':'Nazwa', 'jajko':'sikorka','class':'dupa'}),
            'description':forms.Textarea()
        }
        labels = {
            'name':""
        }




