import django_filters
from .models import Song

class SongFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains',label="Name")
    singer = django_filters.CharFilter(lookup_expr='icontains',label="Singer")
    tags = django_filters.CharFilter(lookup_expr='icontains',label="Tags")
    
    class Meta:
        model = Song
        fields = ["name",'singer',"tags" ]

