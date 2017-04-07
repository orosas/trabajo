from django import forms

class BusquedaForm(forms.Form):
	q = forms.CharField(label = "Sitio", max_length=12)
