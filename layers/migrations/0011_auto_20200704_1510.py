# Generated by Django 2.0.2 on 2020-07-04 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('layers', '0010_auto_20200704_1433'),
    ]

    operations = [
        migrations.AlterField(
            model_name='layersexpenses',
            name='quantity',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
