import django_filters
from django_filters import CharFilter

from . models import *


class todoFilter(django_filters.FilterSet):
    title = CharFilter(field_name='title', lookup_expr='icontains')
    class Meta:
        model = Task
        fields = '__all__'
        exclude = ['complete', 'created']
        

