# Generated by Django 2.2.6 on 2020-01-27 09:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pic', models.FileField(blank=True, null=True, upload_to='profilepics')),
                ('areyou', models.CharField(choices=[('Employer', 'Employer'), ('Jobseeker', 'Jobseeker')], default='jobseeker', max_length=64)),
                ('otp', models.IntegerField()),
                ('registered_date', models.DateTimeField(auto_now_add=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]