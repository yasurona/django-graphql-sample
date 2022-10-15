from django.db import models

class Player(models.Model):
    name = models.CharField(help_text='名前', max_length=50)
    nationality = models.ForeignKey('Country', help_text='国籍', on_delete=models.PROTECT)
    born_on = models.DateField(help_text='生年月日')
    blood_type = models.ForeignKey('BloodType', help_text='血液型', on_delete=models.PROTECT)

    def __str__(self):
        return self.name

    class Meta:
        app_label = 'sampleapp'
