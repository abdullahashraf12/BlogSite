from django.contrib import admin
from userauths.models import User,Profile
from django.utils.html import format_html

# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ["username","email"]
admin.site.register(User,UserAdmin)

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ["display_profile_picture","user", "bio"]

    def display_profile_picture(self, obj):
        if obj.profile_picture:
            return format_html('<img src="{}" style="max-height: 80px; max-width: 80px; border-radius:50%; "/>', obj.profile_picture.url)
        else:
            return '(No image)'

    display_profile_picture.short_description = 'Profile Picture'
admin.site.register(Profile,UserProfileAdmin)
