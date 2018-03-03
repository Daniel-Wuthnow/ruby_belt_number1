# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect

from .models import User, Product
# Create your views here.
def index(request):
	if 'errors' not in request.session:
		request.session['errors'] =[]
	contex = {
		'errors':request.session['errors']
	}
	request.session['errors'] = None
	return render(request , 'first_app/index.html', contex)

def home(request):
	contex = {
		'current_user':User.objects.get(id=request.session['user_id']),
		'my_list':Product.objects.filter(added_by=User.objects.get(id=request.session['user_id'])),
		'their_list':Product.objects.exclude(added_by=User.objects.get(id=request.session['user_id'])),
	}
	return render(request, 'first_app/home.html', contex)

def login(request):
	if request.method == "POST":
		errors = User.objects.login_validation(request.POST)
		if len(errors) != 0:
			request.session['errors'] = errors
			return redirect('/')
		user = User.objects.login(request.POST)
		request.session['user_id'] = user.id
		return redirect('/home')

def register(request):
	if request.method == "POST":
		errors = User.objects.register_validation(request.POST)
		if len(errors) != 0:
			request.session['errors'] = errors
			return redirect('/')
		user = User.objects.register(request.POST)
		request.session['user_id'] = user.id
		return redirect('/home')


def logout(request):
	request.session.clear()
	return redirect('/')

def add(request):
	contex = {
		'current_user':User.objects.get(id=request.session['user_id']),
		'errors':request.session['errors'],
	}
	request.session['errors'] = None
	return render(request, 'first_app/add.html', contex)

def create(request):
	if request.method == "POST":
		errors = Product.objects.product_validation(request.POST)
		if len(errors) != 0:
			request.session['errors'] = errors
			return redirect('/wish_items/create')
		product = Product.objects.product_add(request.POST)
		user = User.objects.get(id=request.session['user_id'])
		user.items.add(product)
		return redirect('/home')

def show(request, number):
	contex = {
		'item':Product.objects.get(id=number),
		'user':Product.objects.get(id=number).added_by.all()
	}
	return render(request, 'first_app/show.html', contex)

def destroy(request, number):
	Product.objects.product_delete(number)
	return redirect('/home')

def join(request, number):
	user = User.objects.get(id=request.session['user_id'])
	item = Product.objects.get(id=number)
	user.items.add(item)
	return redirect('/home')

def remove(request, number):
	user = User.objects.get(id=request.session['user_id'])
	item = Product.objects.get(id=number)
	item.added_by.remove(user)
	return redirect('/home')