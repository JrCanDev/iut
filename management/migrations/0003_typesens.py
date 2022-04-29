# Generated by Django 4.0.3 on 2022-04-12 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0002_detailservice'),
    ]

    operations = [
        migrations.CreateModel(
            name='TypesEns',
            fields=[
                ('type_ens', models.CharField(max_length=8, primary_key=True, serialize=False)),
                ('detail', models.CharField(max_length=50)),
                ('coef_finan', models.FloatField()),
                ('coef_temps', models.FloatField()),
            ],
        ),
    ]