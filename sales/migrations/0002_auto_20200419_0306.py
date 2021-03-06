# Generated by Django 2.0.2 on 2020-04-19 00:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sales',
            name='email',
            field=models.EmailField(default='wallykipps@gmail.com', max_length=255),
        ),
        migrations.AddField(
            model_name='sales',
            name='product',
            field=models.CharField(default='Eggs', max_length=255),
        ),
        migrations.AlterField(
            model_name='sales',
            name='date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='sales',
            name='units',
            field=models.IntegerField(),
        ),
    ]
