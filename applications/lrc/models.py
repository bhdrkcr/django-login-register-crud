# Standard Library
import os
import uuid

# Django
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.contrib.sites.models import Site
from django.core.mail import send_mail
from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _

__all__ = ['User', 'Register']


class UserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """

    def create_user(self, email, password, **extra_fields):
        """
        Create and save a User with the given email and password.
        """
        if not email:
            raise ValueError(_('The Email must be set'))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """

        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self.create_user(email, password, **extra_fields)


def get_file_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'
    return os.path.join('users/avatars', filename)


class User(AbstractUser):
    username = None
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = UserManager()
    email = models.EmailField(_('email address'), unique=True)
    first_name = models.CharField(_('first name'), max_length=50, blank=True)
    last_name = models.CharField(_('last name'), max_length=50, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    avatar = models.ImageField(
        _('User Avatar'),
        upload_to=get_file_path,
        height_field=None,
        width_field=None,
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.email

    def get_full_name(self):
        params = {'first_name': self.first_name, 'middle_name': ' ', 'last_name': self.last_name}
        full_name = '{first_name}{last_name}'.format(**params)
        return full_name.strip()

    @property
    def image_url(self):
        if self.avatar and hasattr(self.avatar, 'url'):
            return self.avatar.url
        else:
            return None


class Register(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def send_registration_mail(self):
        current_site = Site.objects.get_current()
        send_mail(
            _("Verification for email"),
            _("click here to verify: ") + current_site.domain + "verification_key" + str(self.uuid),
            "app@gmail.com",
            [self.user.email],
            fail_silently=False,
        )
