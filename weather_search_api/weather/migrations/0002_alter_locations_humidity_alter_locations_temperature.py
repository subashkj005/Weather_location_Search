# Generated by Django 5.0.6 on 2024-06-13 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weather', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='locations',
            name='humidity',
            field=models.DecimalField(decimal_places=3, max_digits=3),
        ),
        migrations.AlterField(
            model_name='locations',
            name='temperature',
            field=models.DecimalField(decimal_places=3, max_digits=3),
        ),
    ]
