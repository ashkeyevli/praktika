# Generated by Django 2.2.2 on 2019-06-10 18:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_auto_20190610_1656'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='due_on',
            field=models.DateTimeField(blank=True, verbose_name=datetime.datetime(2019, 7, 1, 0, 32, 28, 108750)),
        ),
    ]