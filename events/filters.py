import django_filters
from django_filters import DateFilter, CharFilter

from .models import *


class EventsFilter(django_filters.FilterSet):
    start_date = DateFilter(field_name='date', lookup_expr='gte')
    end_date = DateFilter(field_name='date', lookup_expr='lte')
    name = CharFilter(field_name='name', lookup_expr='icontains')
    description = CharFilter(field_name='description', lookup_expr='icontains')
    class Meta:
        model = Events
        fields = '__all__'
        exclude = ['coordinates', 'date']