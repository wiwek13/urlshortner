# Generated by Django 3.0 on 2019-12-14 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WirrURL',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=220)),
                ('shortcode', models.CharField(max_length=15, unique=True)),
                ('updated', models.DateField(auto_now=True)),
                ('timestamp', models.DateField()),
            ],
        ),
    ]
