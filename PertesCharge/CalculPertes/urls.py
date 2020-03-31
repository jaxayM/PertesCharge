from django.conf.urls import url
from CalculPertes import views

from . import views

urlpatterns = [
    url(r'^formpage/', views.form_view, name='form'),
    url(r'^$', views.index, name='index'),    
]