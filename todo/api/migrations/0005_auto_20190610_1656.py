# Generated by Django 2.2.2 on 2019-06-10 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_task'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='due_on',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.CharField(default='IN PROGRESS', max_length=50),
        ),
    ]
