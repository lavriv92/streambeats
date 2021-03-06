from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin

from .models import User, FriendCircle
from .forms import UserCreationForm, UserChangeForm


admin.site.unregister(Group)


class UserAdmin(UserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
    fields = ('username', 'email', 'password', 'first_name', 'last_name')
    fieldsets = ()
    list_display = ('username', 'email', 'first_name', 'last_name',)
    filter_horizontal = ()
    list_filter = ('is_admin', )
    search_fields = ('username', )


class FriendCircleAdmin(admin.ModelAdmin):
    list_display = ('name', )


admin.site.register(User, UserAdmin)
admin.site.register(FriendCircle, FriendCircleAdmin)
