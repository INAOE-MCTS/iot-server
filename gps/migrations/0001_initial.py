# Generated by Django 4.2.1 on 2023-05-04 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DataModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latitud', models.CharField(blank=True, max_length=50, null=True)),
                ('longitud', models.CharField(blank=True, max_length=50, null=True)),
                ('fecha', models.CharField(blank=True, max_length=50, null=True)),
                ('hora', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
    ]