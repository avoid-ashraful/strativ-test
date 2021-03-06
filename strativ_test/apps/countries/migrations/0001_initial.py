# Generated by Django 3.1.7 on 2021-04-05 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('alpha_code2', models.CharField(max_length=50)),
                ('alpha_code3', models.CharField(max_length=50, unique=True)),
                ('capital', models.CharField(max_length=100)),
                ('population', models.CharField(max_length=100)),
                ('timezones', models.JSONField()),
                ('flag', models.URLField(blank=True, null=True)),
                ('languages', models.JSONField()),
                ('neighbouring_countries', models.JSONField()),
            ],
        ),
    ]
