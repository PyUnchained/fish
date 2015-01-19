import datetime

from django import forms

from models import ProductItem

#Defines the order form used, and it inherits from a previously defined
#model, in this case, ProductItem.
class BasicOrderForm(forms.ModelForm):

	#FREQUENCIES and DAYS represents the options available for selection
	#when the form is rendered. The tuples represent
	#([database_value],[human_readable_value])
	FREQUENCIES = (
		('S','Single Order'),
		('W','Weekly Order'),
	)

	DAYS = (
		('M','Monday'),
		('D','Tuesday'),
		('W','Wednesday'),
		('TH','Thursday'),
		('F','Friday'),
		('S','Saturday'),
	)

	#For the frequency and days fields I have changed the default rendering
	#of the widgets so that they are easier to select. Note that the choices
	#available to each field have also been defined.
	frequency = forms.ChoiceField(choices = FREQUENCIES, widget=forms.RadioSelect)
	days = forms.MultipleChoiceField(choices = DAYS, widget=forms.CheckboxSelectMultiple)

	#For the duration field (and a few others below) I have also changed the
	#html properties of the input field. In this case, it is to display some
	#placeholder text.
	duration = forms.IntegerField(min_value = 1, max_value = 52, initial = 1,
		widget=forms.NumberInput(
		attrs={'placeholder':'How long to repeat order.'}))
	quantity = forms.IntegerField(min_value = 1, max_value = 100)

	#Basically, any html attribute can be altered, as in this case where there
	#is a placeholder as well as a change to the class attribute of the field
	#to make the css easier.
	address_street = forms.CharField(max_length = 100, widget=forms.Textarea(
		attrs={'class':'order-address', 'placeholder':'Enter your address here.'}))
	date = forms.DateField(widget=forms.TextInput(
		attrs={'placeholder':'Any date from tomorrow on.'}))
	num = forms.IntegerField(widget=forms.TextInput(
		attrs={'placeholder':'Your number (no spaces).'}))


	#The meta field is required since my form is ultimately based off of a model
	#saved in the database.
	class Meta:

		#The model object (you'll notice I imported it earlier).
		model = ProductItem

		#The fields to use from the model. You must explicitly define either the 
		#fields you want, as I've done here, or the list of fields to exclude
		#by setting the exclude attribute instead.
		fields = ('name', 'price')

		#I have also overriden some of the default widgets, because I don't
		#want people to be able to edit the name and price once the form is
		#rendered.
		widgets = {
			'name': forms.TextInput(attrs={'readonly':True}),
			'price': forms.TextInput(attrs={'readonly':True})
		}

	def clean_date(self):
		selected_date = self.cleaned_data['date']
		tomorrow = datetime.date.today() + datetime.timedelta(
			days = 1)

		if selected_date < tomorrow:
			raise forms.ValidationError("Order date must be from tomorrow onwards.")

		return selected_date
