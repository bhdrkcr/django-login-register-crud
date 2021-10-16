# Third Party
from rest_framework import routers

# Local Folder
from .views import UserViewSet, VerificationViewSet

app_name = 'lrc'


router = routers.SimpleRouter()
router.register(r'users', UserViewSet, basename='users')
router.register(r'verification', VerificationViewSet, basename='verification')

urlpatterns = []

urlpatterns += router.urls
