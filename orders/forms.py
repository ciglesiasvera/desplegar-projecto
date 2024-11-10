from django import forms
from .models import Order, Product

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['product', 'quantity']

class ReportFilterForm(forms.Form):
    product = forms.ModelChoiceField(queryset=Product.objects.all(), required=False, label="Producto")
    start_date = forms.DateField(required=False, widget=forms.DateInput(attrs={'type': 'date'}), label="Fecha de inicio")
    end_date = forms.DateField(required=False, widget=forms.DateInput(attrs={'type': 'date'}), label="Fecha de fin")
    min_quantity = forms.IntegerField(required=False, label="Cantidad mínima")
    max_quantity = forms.IntegerField(required=False, label="Cantidad máxima")
