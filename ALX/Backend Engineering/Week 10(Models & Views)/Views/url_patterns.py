#Define urls
from django.urls import path
from . import views

urlpatterns = [
    path('my-message/', views.my_message, name='my_message'),
    path('my-template/', views.MyTemplateView.as_view(), name='my_template'),
]