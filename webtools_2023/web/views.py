import random
from django.views import generic as views
from django.http import HttpResponse
from django.views.decorators.cache import cache_page

from webtools_2023.web.models import Employee

CLICKS_COUNT_SESSION_KEY = 'CLICKS_COUNT_SESSION_KEY'
LATEST_VALUE_SESSION_KEY = 'LATEST_VALUE_SESSION_KEY'

def very_slow_operation():
    random.randint(1, 1024)


@cache_page(1*60)
def index(request):
    clicks_count = request.session.get(CLICKS_COUNT_SESSION_KEY, 0) + 1
    request.session[CLICKS_COUNT_SESSION_KEY] = clicks_count

    value = very_slow_operation()

    latest_value = request.session.get(LATEST_VALUE_SESSION_KEY, [])
    latest_value = [value] + latest_value
    latest_value = latest_value[:3]
    request.session[LATEST_VALUE_SESSION_KEY] = latest_value

    return HttpResponse(f'The value is {value}; {", ".join(str(x) for x in latest_value)}')


class EmployeesListView(views.ListView):
    model = Employee
    template_name = 'employees/list.html'
    # paginate_by = 4

    def get_paginate_by(self, queryset):
        return random.randint(3,10)


