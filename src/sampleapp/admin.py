from django.contrib import admin
from django.apps import apps

models = apps.get_app_config('sampleapp').get_models()
for model in models:
    admin.site.register(model)
