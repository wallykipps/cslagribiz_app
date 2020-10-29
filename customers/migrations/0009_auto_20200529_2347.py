# Generated by Django 2.0.2 on 2020-05-29 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0008_auto_20200514_2330'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customers',
            options={'ordering': ['-reg_date']},
        ),
        migrations.AlterField(
            model_name='customers',
            name='firstname',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='customers',
            name='lastname',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='customers',
            name='location',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='customers',
            name='phonenumber',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='customers',
            name='reg_date',
            field=models.DateField(),
        ),
    ]
