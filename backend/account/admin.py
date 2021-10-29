from django.contrib import admin

# Register your models here.
from account.models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'first_name', 'job')
    list_filter = ('job',)

    fieldsets = (
        ('Info', {
            'fields': ('username', 'password', 'first_name', 'last_name', 'email')
        }),
        ('Job', {
            'fields': ('job',)
        }),
        ('Permission', {
            'fields': ('is_staff', 'is_active', 'is_superuser')
        }),
        ('Date', {
            'fields': ('date_joined', 'last_login')
        })
    )
