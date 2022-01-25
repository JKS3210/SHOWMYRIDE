from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import numpy as np
import pandas as pd
import sklearn
from sklearn.neighbors import NearestNeighbors
from carapp.models import CarDetails

# Create your views here.
def home(request):
    context = {}
    template = loader.get_template("home.html")
    return HttpResponse(template.render(context, request))

def index(request):
    context = {}
    template = loader.get_template("index.html")
    return HttpResponse(template.render(context, request))

def about(request):
    context = {}
    template = loader.get_template("about.html")
    return HttpResponse(template.render(context, request))

def viewres(request):
    if request.method=="POST":
        year=request.POST.get("year")
        price = request.POST.get("price")
        km_driven = request.POST.get("km")
        fuel = request.POST.get("fuel")
        m=[]
        m.append(year)
        m.append(price)
        m.append(km_driven)
        m.append(fuel)
        v=CarDetails.objects.all().values()
        v1=pd.DataFrame(v)

        X = v1.loc[:, ('year', 'selling_price', 'km_driven', 'fuel',)].values
        X[0:5]

        nn = NearestNeighbors(n_neighbors=5).fit(X)
        temp = nn.kneighbors([m])
        x = temp[1]
        y = x[0]
        z = int(y[0])
        d=CarDetails.objects.raw("SELECT * from carapp_cardetails WHERE id='%s'",[z])
        context = {'k': d}
        template = loader.get_template("viewresult.html")
        return HttpResponse(template.render(context, request))
