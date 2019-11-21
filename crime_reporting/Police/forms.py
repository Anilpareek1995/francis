from django import forms
from .models import Missing
class MissingForm(forms.ModelForm):
    name = forms.CharField(required=False)
    mobile = forms.IntegerField(required=False)
    address = forms.CharField(widget=forms.Textarea(attrs={"rows":4, "cols":15}),required=False)
    city = forms.CharField(required=False)
    details = forms.CharField(widget=forms.Textarea(attrs={"rows":4, "cols":15}),required=False)

    class Meta:
        model = Missing
        fields = '__all__'

