from django import forms
from django import forms

from .models import OrderNew


class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = OrderNew
        fields = ['first_name', 'last_name', 'email', 'telephone', 'address', 'postal_code', 'city']



