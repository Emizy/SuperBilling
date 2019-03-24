from django.apps import apps
from django.contrib import messages
from django.contrib.auth import authenticate, login as l
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.template.loader import render_to_string
from django.views.generic import View, TemplateView
from rest_framework.decorators import api_view
from datetime import date, datetime, timedelta

from .models import *


# Create your views here.
def index(request):
    if request.method == 'GET':
        total_user = User.objects.all().count()
        total_item = service.objects.all().count()
        total_bill = cycle.objects.all().count()
        context = {
            'user': total_user,
            'item': total_item,
            'bill': total_bill
        }
        return render(request, 'index.html', context)


class CrudView(View):
    def get(self, request):
        user = User.objects.all()

        context = {
            'users': user,
        }
        return render(request, 'add_user.html', context)

    def post(self, request):
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        print(name)
        context = {}
        try:
            exist = User.objects.filter(email=email)
        except:
            exist = None
        if exist:
            context['status'] = 400
            context['message'] = "Email Already Exist"
        else:
            user = User()
            user.name = name
            user.email = email
            user.number = phone
            user.address = address
            user.save()
            context['message'] = "User successfully added"
            context['status'] = 200

        return JsonResponse(context, status=context['status'])


class BillView(View):
    def get(self, request):
        bill = cycle.objects.all()
        user = User.objects.all()
        items = service.objects.all()
        context = {
            'bills': bill,
            'users': user,
            'items':items
        }
        return render(request, 'billing.html', context)

    def post(self, request):
        context = {}
        client = User.objects.get(id=request.POST.get('client'))
        type = request.POST.get('bill_type')
        description = request.POST.get('description')
        price = request.POST.get('price')
        item = request.POST.getlist('item[]')
        bill = cycle()
        bill.type = type
        bill.user = client
        bill.description = description
        bill.price = price
        bill.item = item
        bill.status = "NO"
        bill.created = date.today()
        bill.save()
        context['status'] = 200
        context['message'] = 'Billing Successfully Added'
        return JsonResponse(context, status=context['status'])


class ItemView(View):
    def get(self, request):
        item = service.objects.all()
        context = {
            'item': item,
        }
        return render(request, 'add_item.html', context)

    def post(self, request):
        context = {}
        item = request.POST.get('item')
        exist = ""
        try:
            exist = service.objects.filter(item=item)
        except:
            pass
        if exist:
            context['status'] = 400
            context['message'] = 'Item Already Exist'
            return JsonResponse(context, status=context['status'])
        else:
            items = service()
            items.item = item
            items.save()
            context['status'] = 200
            context['message'] = 'Billing Successfully Added'
            return JsonResponse(context, status=context['status'])
