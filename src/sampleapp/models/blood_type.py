from django.db import models

class BloodType(models.Model):
    name = models.CharField(help_text='血液型', max_length=5)

    def __str__(self):
        return self.name

    class Meta:
        app_label = 'sampleapp'
