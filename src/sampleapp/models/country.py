from django.db import models

class Country(models.Model):
    name = models.CharField(help_text='国名', max_length=50)

    class Meta:
        app_label = 'sampleapp'
