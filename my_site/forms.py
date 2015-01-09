from django import forms

from models import ProductItem

class BasicOrderForm(forms.ModelForm):

	FREQUENCIES = (
		('O','Single Order'),
		('D','Weekly Order'),
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
	quantity = forms.IntegerField(min_value = 1, max_value = 100)
	address_street = forms.CharField(max_length = 100, widget=forms.Textarea(
		attrs={'class':'order-address', 'placeholder':'Enter your address here.'}))
	date = forms.DateField(widget=forms.TextInput(
		attrs={'placeholder':'Any date from tomorrow on.'}))
	num = forms.IntegerField(widget=forms.TextInput(
		attrs={'placeholder':'Your number (no spaces).'}))

	class Meta:
		model = ProductItem
		fields = ('name', 'price')
		widgets = {
			'name': forms.TextInput(attrs={'readonly':True}),
			'price': forms.TextInput(attrs={'readonly':True})
		}
