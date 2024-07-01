from rest_framework import generics, pagination, filters
from django.shortcuts import render
from .models import Log
from .serializers import LogSerializer

class LogPagination(pagination.PageNumberPagination):
    page_size = 100
    page_size_query_param = 'page_size'
    max_page_size = 1000

class LogApiView(generics.ListAPIView):
    queryset = Log.objects.all()
    serializer_class = LogSerializer
    # Пагинация, фильтр по указанным полям 
    pagination_class = LogPagination
    filter_backends = [filters.SearchFilter]
    search_fields = ['ip', 'URI', 'userAgent']