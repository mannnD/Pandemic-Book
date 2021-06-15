# Generated by Django 3.1.7 on 2021-06-01 16:16

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mypost',
            name='City',
            field=models.CharField(max_length=264, validators=[django.core.validators.RegexValidator('^[A-Z]*$', 'Only uppercase letters allowed.')], verbose_name='Enter Your City'),
        ),
    ]