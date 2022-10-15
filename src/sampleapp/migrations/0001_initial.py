# Generated by Django 3.2 on 2022-10-15 13:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BloodType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='血液型', max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='国名', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='名前', max_length=50)),
                ('born_on', models.DateField(help_text='生年月日')),
                ('blood_type', models.ForeignKey(help_text='血液型', on_delete=django.db.models.deletion.PROTECT, to='sampleapp.bloodtype')),
                ('nationality', models.ForeignKey(help_text='国籍', on_delete=django.db.models.deletion.PROTECT, to='sampleapp.country')),
            ],
        ),
    ]
