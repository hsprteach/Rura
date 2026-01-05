from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .forms import LearnerDetail

# Create your views here.

def home(request):
    form = LearnerDetail()
    if request.method == 'POST':
        form = LearnerDetail(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Success")
        
    return render(request, 'index.html', {'form' : form})    

def learners_fn(request):
    return HttpResponse("<h1>Hi from func view</h1>")

class Learners_cls(View):
    def get(self, request):
        return HttpResponse("<h1>Hi from class view</h1>")
