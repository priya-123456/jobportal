# Generated by Django 2.2.4 on 2020-01-08 04:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appnewjob', '0002_auto_20200107_1521'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='resume',
            name='specialization',
        ),
        migrations.DeleteModel(
            name='Specialization',
        ),
    ]
