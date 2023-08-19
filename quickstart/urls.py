from django.urls import include, path, re_path
from rest_framework import routers
from quickstart import views
from .parsers_views import FileUploadView
from .renders_views import UserCount


router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('practice_users/', views.ListUsers.as_view()),
    path('practice_view02/', views.view02),
    re_path(r'^upload/(?P<filename>[^/]+)$', FileUploadView.as_view()),
    path('render_users/', UserCount.as_view())
]