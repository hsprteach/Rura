from django.urls import path
from . import views

urlpatterns = [
    path('func', views.learners_fn),
    path('cls', views.Learners_cls.as_view()), 
]