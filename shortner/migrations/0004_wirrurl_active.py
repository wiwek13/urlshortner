# Generated by Django 3.0 on 2019-12-16 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shortner', '0003_auto_20191216_1440'),
    ]

    operations = [
        migrations.AddField(
            model_name='wirrurl',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]
