from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from views import UserSerializer
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser, IsAuthenticated


class UserViewSet(viewsets.ViewSet):
    """
    A Simple ViewSet for listing or retrieving users.
    """
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def list(self, request):
        queryset = User.objects.all()
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = User.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)


    def create(self, request):
        pass

    def update(self, request, pk=None):
        pass

    def partial_update(self, request, pk=None):
        pass

    def destroy(self, request, pk=None):
        pass


    def get_permissions(self):
        if self.action == 'list':
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]


class UserViewSet2(viewsets.ModelViewSet):
    """
    A viewset that provides the stanard actions
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


    def set_password(self, request, pk=None):
        user = self.get_object()

