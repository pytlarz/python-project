# Generated by Django 2.2.2 on 2019-06-18 19:40

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=200)),
                ('postalCode', models.CharField(max_length=10)),
                ('latitude', models.CharField(max_length=50)),
                ('longitude', models.CharField(max_length=50)),
                ('phoneNumber', models.CharField(max_length=20)),
                ('websiteUrl', models.CharField(max_length=200)),
                ('facebookUrl', models.CharField(max_length=200)),
                ('cityName', models.CharField(max_length=200)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
