from django import forms
from .models import Cliente


class ClienteForm(forms.ModelForm):
    # specify the name of model to use
    class Meta:
        model = Cliente
        fields = "__all__"
