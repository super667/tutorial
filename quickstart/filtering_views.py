from .models import Purchase
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics

class UserListView(generics.ListAPIView):
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['category', 'in_stock']

    