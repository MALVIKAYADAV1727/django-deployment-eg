from django.urls import path, include
from appOne import views

urlpatterns=[
path('formN/', views.formNameView, name='formNameView'),
]
