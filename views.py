# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import datatable1
# Create your views here.from .models import datatable1
def enterdetails(request):
    return render(request,"enterdetails.html")
def savedetails(request):
    food1=request.POST["t1"]
    trip1=request.POST["t2"]
    shopping1=request.POST["t3"]
    v=datatable1(food=food1,trip=trip1,shopping=shopping1)
    v.save()
    return HttpResponse(request,"succuss")

total_Expense =0
def calculate_expense(request):
    objects = datatable1.objects.all()
    for i in objects:
        total_Expense+=i
    return HttpResponse(request,'total_Expense')

