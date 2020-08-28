from django.contrib import admin
from .models import Contact

list_display = ['__all__']

admin.site.register(Contact)
