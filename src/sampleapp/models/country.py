from django.db import models

class Country(models.Model):
    name = models.CharField(help_text='国名', max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        app_label = 'sampleapp'
