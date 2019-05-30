from django.shortcuts import render
from .models import Portfolio
# Create your views here.
# def portfolio(request):
#     return render(request,'portfolio.html')

def portfolio(request):
    portfolios=Portfolio.objects
    return render(request,'portfolio.html',{'portfolios':portfolios})  

    