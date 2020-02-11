# Generated by Django 2.2.6 on 2020-02-04 07:02

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('appnewjob', '0003_auto_20200131_1516'),
    ]

    operations = [
        migrations.AddField(
            model_name='createjob',
            name='role',
            field=models.CharField(default=datetime.datetime(2020, 2, 4, 7, 2, 27, 603971, tzinfo=utc), max_length=50),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='Shortlist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seejer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appnewjob.Resume')),
                ('users', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]