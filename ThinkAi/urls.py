from django.urls import path
from . import views

urlpatterns = [
    path('', views.hi_view, name='hi'),
    path('about/', views.about_view, name='about'),

]
