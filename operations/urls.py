from django.urls import path
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', login_required(TemplateView.as_view(template_name='operations/operations_home.html'), login_url='login'), name='operations_home'),
]