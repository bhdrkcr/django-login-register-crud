# Third Party
from rest_framework import routers

# Local Folder
from .views import UserViewSet

app_name = 'lrc'


router = routers.SimpleRouter()
router.register(r'users', UserViewSet, basename='users')

urlpatterns = []

urlpatterns += router.urls
