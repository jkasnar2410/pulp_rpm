# Generated by Django 2.2.13 on 2020-06-24 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rpm', '0013_RAW_rpm_evr_extension'),
    ]

    operations = [
        migrations.AddField(
            model_name='rpmrepository',
            name='retain_package_versions',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
