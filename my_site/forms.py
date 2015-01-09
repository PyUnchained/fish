from django import forms

from models import ProductItem

class BasicOrderForm(forms.ModelForm):

	FREQUENCIES = (
		('O','Single Order'),
		('D','Repeat Order'),
	)

	DAYS = (
		('M','Monday'),
		('D','Tuesday'),
		('W','Wednesday'),
		('TH','Thursday'),
		('F','Friday'),
		('S','Saturday'),
	)

	frequency = forms.ChoiceField(choices = FREQUENCIES, widget=forms.RadioSelect)
	days = forms.MultipleChoiceField(choices = DAYS, widget=forms.CheckboxSelectMultiple)
	duration = forms.IntegerField(min_value = 1, max_value = 52)

	class Meta:
		model = ProductItem
		fields = ('name', 'price')
