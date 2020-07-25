from django.shortcuts import render
from django.http import HttpResponse


def homePageView(request):
    return HttpResponse('<h1>HOME-PAGE</h1>')


