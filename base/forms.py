from django import forms
from .models import Dataset


class DatasetForm(forms.ModelForm):
  class Meta:
    model = Dataset
    fields = "__all__"
    exclude = ["overview"]