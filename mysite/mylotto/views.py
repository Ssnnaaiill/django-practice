from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def LottoIndex(request):
    return HttpResponse('<h1>로또앱 index!</h1>')
