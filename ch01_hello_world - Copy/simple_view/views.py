from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.views.generic import TemplateView


def index(request):
    return HttpResponse('Hello, World!')


class HelloPageView(TemplateView):
    template_name = 'hello.html'

class HelloUserPageView(TemplateView):
    template_name = 'hello_user.html'