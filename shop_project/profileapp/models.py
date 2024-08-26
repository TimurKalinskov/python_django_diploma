from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.core.validators import RegexValidator
# Create your models here.
from django.core.exceptions import ValidationError

from .managers import MyUserManager


class User(AbstractBaseUser):
    def validate_image(self, fieldfile_obj):
        filesize = fieldfile_obj.file.size
        megabyte_limit = 2.0
        if filesize > megabyte_limit * 1024 ** 2:
            raise ValidationError("Max file size is %sMB" % str(megabyte_limit))

    full_name = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    email = models.EmailField(unique=True)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$')
    phone_number = models.CharField(validators=[phone_regex], max_length=17)
    avatar = models.ImageField(validators=[validate_image])
    password = models.CharField(max_length=1000)

    objects = MyUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['phone_number', 'username', 'email']

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin
