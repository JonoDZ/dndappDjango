from django.apps import apps
from django.contrib import admin
myapp = apps.get_app_config('worldgen')

admin.site.register(myapp.models.values())
