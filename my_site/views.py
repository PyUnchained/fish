import time
import json
import zmq

from django.shortcuts import render, render_to_response, redirect
from django.template import Context, RequestContext
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.core.urlresolvers import reverse
# Create your views here.

from forms import BasicOrderForm
from models import ProductItem, Order

def home(request):
	""" Handles requests for the home page """

	return render(request, 'home.html')

def order_steps(request, step, variable = None):
	"""Handles online orders in a ste-by-step manner, as opposed to
	using ajax, which works horribly on most mobile browsers."""

	#First step: choosing your product.
	if int(step) == 1:
		#Provides a list of all products saved in the database to be used in
		#the template to create the option buttons.
		products = ProductItem.objects.all()

		#Note that the last argument in this function is a dictionary. This
		#defines what data will be available for me to use with the template
		#tags, in this case a list of all the products stored in the database.
		return render(request, 'orders_step1.html',
			{'products':products})

	#Second step: give the details of your order
	if int(step) == 2:

		products = ProductItem.objects.all()

		#Create the correct form for the product and rename the variable
		#string for clarity.
		for product in products:
			meal_type = variable

			#Match the type of meal desired to the name of a
			#product saved in the database
			if meal_type == product.name:

				#Initialize the form with the name of the desired
				#product and its price.
				form = BasicOrderForm(initial = {'name':product.name,
					'price':product.price})

				return render(request, 'orders_step2.html',
					{'form':form,})

	#Third step: validate and save the order
	if int(step) == 3:
		if request.method == "POST":
			#Get the info from the form that has been posted
			form = BasicOrderForm(request.POST)

			#Check that the form is valid
			if form.is_valid():
				allclean = form.cleaned_data

				#Find the grand total for the order and the object that
				#represents the desired product.
				grand_total = int(allclean['price'])*int(allclean['quantity'])
				product = ProductItem.objects.get(name = allclean['name'])

				#Create a new order record and save it to the database.
				new_order = Order.objects.create(
					days = str(allclean['days']),
					date = allclean['date'],
					frequency = allclean['frequency'],
					duration = allclean['duration'],
					address_street = allclean['address_street'],
					quantity = allclean['quantity'],
					num = allclean['num'],
					total = grand_total,
					product = product)

				#Go to the success confirmation page and also provide
				#the order id for customers to check their order
				#status later.
				return render(request, 'orders_step3.html',
					{'order_num':new_order.pk})

			#If the form is invalid, return the form object and display
			#the errors.
			else:
				return render(request, 'orders_step2.html',
					{'form':form})

	#Fourth step: payment method.
	

	return render(request, 'orders.html')


def test(request):
	"""This was a test function, representing the asynchronous client
	communicating with the background process defined in
	test_new_server.py.
	"""

	#Get a context, define the type of socket to use and bind to the
	#correct port to start sending messages.
	cxt = zmq.Context()
	send_socket = cxt.socket(zmq.PUSH)
	send_socket.bind("tcp://127.0.0.1:5000")

	#Define the work for the consumer processes to deal with and send
	#it in json format.
	work = {'type':'wrong','msg':'Some Message'}
	send_socket.send_json(work)

	#Return a message stating that the communication was carried out,
	#though the process may have failed, there is no way to know
	#at this point as the consumer may still be working in the background
	msg = "Action Completed"

	return render(request, 'msg_back.html',
		{'msg':msg})