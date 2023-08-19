from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'user', UserViewSet)
router.register(r'account', AccountViewSet)

urlpattern = router.urls


