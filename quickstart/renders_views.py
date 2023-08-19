from django.contrib.auth.models import User
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView


class UserCount(APIView):
    """
    A view that return the count of active users in JSON.
    """

    renderer_classes = [JSONRenderer]
    
    def get(self, request, format=None):
        user_count = User.objects.all().count()
        content = {'user_count': user_count}
        return Response(content)

    
from rest_framework.decorators import api_view
from rest_framework.decorators import renderer_classes
from rest_framework.renderers import JSONRenderer

@api_view(["GET"])
@renderer_classes([JSONRenderer])
def user_count_view(request, format=None):
    """
    A view that return the count of active user in JSON.
    """
    user_count = User.objects.all().count()
    content = {'user_count': user_count}
    return Response(content)
