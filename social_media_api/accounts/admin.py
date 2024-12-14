from django.contrib import admin
from django.contrib.auth import get_user_model

# For the default user model
User = get_user_model()

# Registering the user model
admin.site.register(User)