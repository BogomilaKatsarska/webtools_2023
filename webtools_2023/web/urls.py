from .signals import *
from django.urls import path

from webtools_2023.web.views import index, EmployeesListView

urlpatterns = (
    path('', index, name='index'),
    path('employees/', EmployeesListView.as_view(), name='employee list'),
)