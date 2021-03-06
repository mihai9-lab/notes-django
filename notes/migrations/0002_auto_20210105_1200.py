# Generated by Django 3.1.5 on 2021-01-05 11:00

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='colorBackground',
            field=models.CharField(default='#ffffff', max_length=7),
        ),
        migrations.AddField(
            model_name='note',
            name='colorText',
            field=models.CharField(default='#333333', max_length=7),
        ),
        migrations.AddField(
            model_name='note',
            name='completed',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='note',
            name='fontSize',
            field=models.PositiveIntegerField(default=16, validators=[django.core.validators.MaxValueValidator(30, 'Font size has to be less than or equal to 30'), django.core.validators.MinValueValidator(5, 'Font size has to be bigger than or equal to 5')]),
        ),
        migrations.AddField(
            model_name='note',
            name='name',
            field=models.CharField(default='test', max_length=50),
            preserve_default=False,
        ),
    ]
