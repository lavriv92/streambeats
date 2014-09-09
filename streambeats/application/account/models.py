from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class UserManager(BaseUserManager):

    def _create_user(self, username,
                     email, password, first_name=None, last_name=None):
        user = self.model(
            username=username,
            email=email,
            first_name=first_name,
            last_name=last_name
        )
        user.set_password(password)
        return user

    def create_user(self, username,
                    email, password, first_name=None, last_name=None):
        user = self._create_user(
            username=username,
            email=email,
            first_name=first_name,
            last_name=last_name,
            password=password
        )
        user.save()
        return user

    def create_superuser(self, username, password, email=None,
                         first_name=None, last_name=None):
        user = self._create_user(
            username=username,
            password=password,
            email=email,
            first_name=first_name,
            last_name=last_name
        )
        user.is_admin = True
        user.save()
        return user


class User(AbstractBaseUser):
    """
    Custom user model
    """
    email = models.EmailField(
        _('email'),
        max_length=255,
        unique=True,
        blank=True,
        null=True
    )
    username = models.CharField(_('username'), max_length=120, unique=True)
    first_name = models.CharField(_('first_name'), max_length=120,
                                  null=True, blank=True)
    last_name = models.CharField(_('last_name'), max_length=120,
                                 null=True, blank=True)
    created = models.DateTimeField(_('created'), auto_now_add=True)
    updated = models.DateTimeField(_('updated'), auto_now=True)
    is_admin = models.BooleanField(_('is admin'), default=False)

    objects = UserManager()
    USERNAME_FIELD = 'username'

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')
        ordering = ('-created', )

    def __unicode__(self):
        return self.username

    def get_short_name(self):
        return self.username

    def get_full_name(self):
        return self.username

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        return self.is_admin


class FriendCircle(models.Model):
    name = models.CharField(_('name'), max_length=120)
    owner = models.ForeignKey(User, verbose_name=_('owner'))
    members = models.ManyToManyField(
        User,
        related_name='members',
        verbose_name=_('members')
    )

    created = models.DateTimeField(auto_now_add=True,
                                   verbose_name=_('created'))
    updated = models.DateTimeField(auto_now=True,
                                   verbose_name=_('updated'))

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ('created', )
        verbose_name = _('friend circle')
