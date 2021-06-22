from django.conf import settings
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import PermissionsMixin
from django.db import models
import uuid


class Permission(models.Model):
    scope = models.CharField(max_length=255, blank=True, unique=True)
    description = models.CharField(max_length=255, unique=True, null=True)

    def __str__(self):
        return f'{self.scope} ({self.description})'


class Role(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField()
    permissions = models.ManyToManyField(Permission, null=True, related_name="roles")
    is_private = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class UserManager(BaseUserManager):
    def create_user(self, email, password=None):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_staffuser(self, email, password):
        """
        Creates and saves a staff user with the given email and password.
        """
        user = self.create_user(
            email,
            password=password,
        )
        user.staff = True
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        """
        Creates and saves a superuser with the given email and password.
        """
        user = self.create_user(
            email,
            password=password,
        )
        user.staff = True
        user.admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    password = models.CharField(verbose_name='password', max_length=255)
    email = models.EmailField(max_length=255, unique=True, null=True)
    active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False)  # staff not superuser
    admin = models.BooleanField(default=False)  # superuser
    timestamp = models.DateTimeField(auto_now_add=True)
    role = models.ForeignKey(Role, null=True, blank=True, on_delete=models.CASCADE)
    USERNAME_FIELD = 'email'  # username

    objects = UserManager()

    class Meta:
        db_table = 'hr_users'

    def __str__(self):
        return str(str(self.id) + " : " + self.email)

    def has_perm(self, perm, obj=None):  # show the site administration
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.staff

    @property
    def is_active(self):
        return self.active

    @property
    def is_admin(self):
        return self.staff

    def set_password(self, raw_password):
        self.password = make_password(password=raw_password, salt=settings.SECRET_KEY)
        self._password = raw_password
