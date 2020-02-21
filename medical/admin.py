from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .adminform import UserAdminCreationForm, UserAdminChangeForm
from .models import MyUser 


class UserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    form = UserAdminChangeForm
    add_form = UserAdminCreationForm

    list_display = ('id', 'first_name', 'email', 'department', 'role','sex','active', 'admin')
    list_filter = ('admin', 'staff', 'department', 'active')
    list_display_links = ('email',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('department', 'first_name')}),
        ('Permissions', {'fields': ('admin', 'active', 'staff')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('surname', 'email','first_name','department', 'password1', 'password2')}
        ),
    )
    search_fields = ('first_name',)
    ordering = ('first_name',)
    filter_horizontal = ()


admin.site.register(MyUser, UserAdmin)
admin.site.unregister(Group)




