from django.contrib.auth.models import User
from serializers import UserSerializer
from rest_framework import generics
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response


class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser]


class UserList2(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser]

    def list(self, request):
        queryset = self.get_queryset()
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data)

    
    def get_queryset(self):
        user = self.request.user
        return user.accounts.all()


    def get_object(self):
        queryset = self.queryset()
        filter = {}
        for field in self.multiple_lookup_fields:
            filter[field] = self.kwargs[field]

        obj = get_object_or_404(queryset, **filter)
        self.check_object_permissions(self.request, obj)
        return obj


    def filter_queryset(self, queryset):
        filter_backends = [CategoryFilter]

        if 'geo_route' in self.request.query_params:
            filter_backends = [GeoRouterFilter, CategoryFilter]
        elif 'geo_point' in self.request.query_params:
            filter_backends = [GeoPointFilter, CategoryFilter]
        for backend in list(filter_backends):
            queryset = backend().filter_queryset(self.request, queryset, view=self)

        return queryset

from rest_framework.generics import get_object_or_404

class MultipleFieldLookupMixin:
    """
    Apply this minix to any view or viewset to get, multiple field filtering
    based on a 'lookup_fields' attribute, instead of the default single field filtering
    """

    def get_object(self):
        queryset = self.get_queryset()
        queryset = self.filter_queryset(queryset)
        filter = {}
        for field in self.lookup_fields:
            if self.kwargs.get(field):
                filter[field] = self.kwargs[field]
        obj = get_object_or_404(queryset, **filter)
        self.check_object_permissions(self.request, obj)
        return obj
    

class RetrieveUserView(MultipleFieldLookupMixin, generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_fields = ['account', 'username']
