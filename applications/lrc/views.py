# Third Party
from rest_framework import permissions, viewsets

# Local Folder
from .models import Register, User
from .serializer import RegisterSerializer, UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    A ViewSet for viewing and editing the users.
    """

    serializer_class = UserSerializer
    queryset = User.objects.all()

    def get_permissions(self):
        if self.action in ['update', 'partial_update', 'destroy', 'list']:
            self.permission_classes = [permissions.IsAuthenticated]
        elif self.action in ['create']:
            self.permission_classes = [permissions.IsAdminUser]
        elif self.action in ['retrieve']:
            if self.request.user.id == int(self.kwargs['pk']):
                self.permission_classes = [permissions.IsAuthenticated]
            else:
                self.permission_classes = [permissions.IsAdminUser]
        return super(UserViewSet, self).get_permissions()

    def get_queryset(self):
        if self.action == 'list':
            if self.request.user.is_superuser:
                return User.objects.all()
            else:
                return self.queryset.filter(id=self.request.user.id)
        else:
            return super().get_queryset()


class RegisterViewSet(viewsets.ModelViewSet):
    """
    A ViewSet for viewing and editing the users.
    """

    serializer_class = RegisterSerializer
    queryset = Register.objects.all()
