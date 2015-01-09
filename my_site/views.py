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

	return render(request, 'home.html')

def order_steps(request, step, meal_type = None):

	if int(step) == 1:
		products = ProductItem.objects.all()
		return render(request, 'orders_step1.html',
			{'products':products})

	if int(step) == 2:
		products = ProductItem.objects.all()

		for product in products:
			if meal_type == product.name:
				form = BasicOrderForm(initial = {'name':product.name,
					'price':product.price})
				return render(request, 'orders_step2.html',
					{'form':form,
					'product':product})

	if int(step) == 3:
		if request.method == "POST":
			form = BasicOrderForm(request.POST)
			if form.is_valid():
				allclean = form.cleaned_data

				grand_total = int(allclean['price'])*int(allclean['quantity'])
				product = ProductItem.objects.get(name = allclean['name'])

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

				return render(request, 'orders_step3.html',
					{'order_num':new_order.pk})


	

	return render(request, 'orders.html')


def test(request):

	cxt = zmq.Context()
	send_socket = cxt.socket(zmq.PUSH)
	send_socket.bind("tcp://127.0.0.1:5000")

	work = {'type':'wrong','msg':'Some Message'}
	send_socket.send_json(work)

	msg = "Action Completed"

	return render(request, 'msg_back.html',
		{'msg':msg})