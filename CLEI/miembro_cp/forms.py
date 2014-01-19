from django import forms
from .models import MiembroCp


class MiembroCpForm(forms.ModelForm):
    class Meta:
        model = MiembroCp