from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("<h4>Hello</h4>")


def contacts(request):
    return HttpResponse('<h3>Контакты</h3>')