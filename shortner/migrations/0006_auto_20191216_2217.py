# Generated by Django 3.0 on 2019-12-16 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shortner', '0005_auto_20191216_1746'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wirrurl',
            name='shortcode',
            field=models.CharField(blank=True, max_length=15, unique=True),
        ),
    ]
