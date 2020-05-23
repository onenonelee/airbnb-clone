from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models


@admin.register(models.User)  # Register My User model on the admin panel
class CustomUserAdmin(UserAdmin):

    """ Custom User Admin """

    # list_display makes the columns on the admin panel
    list_display = ("username", "email", "gender", "language", "currency", "superhost")

    # list_display makes a sidebar on the admin panel with those filters
    list_filter = ("language", "currency", "superhost")

    # fildsets makes things that I can modify on the admin user panel
    # UserAdmin already has things, so I add up Custom Profile to UserAdmin
    fieldsets = UserAdmin.fieldsets + (
        (
            "Custom Profile",
            {
                "fields": (
                    "avatar",
                    "gender",
                    "bio",
                    "birthdate",
                    "language",
                    "currency",
                    "superhost",
                )
            },
        ),
    )

    list_filter = UserAdmin.list_filter + ("superhost",)

    list_display = (
        "username",
        "first_name",
        "last_name",
        "email",
        "is_active",
        "language",
        "currency",
        "superhost",
        "is_staff",
        "is_superuser",
    )
