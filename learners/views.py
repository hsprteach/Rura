from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

# Create your views here.
def learners_fn(request):
    return HttpResponse("<h1>Hi from func view</h1>")

class Learners_cls(View):
    def get(self, request):
        return HttpResponse("<h1>Hi from class view</h1>")
