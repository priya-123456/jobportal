# Generated by Django 2.2.4 on 2020-01-08 10:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appnewjob', '0003_auto_20200108_0945'),
    ]

    operations = [
        migrations.RenameField(
            model_name='resume',
            old_name='university_name',
            new_name='university_name_collage_name_school_name',
        ),
        migrations.AlterField(
            model_name='resume',
            name='expect_package',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appnewjob.Package'),
        ),
    ]
