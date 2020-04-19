# Generated by Django 2.0.2 on 2020-04-18 23:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('customer', models.CharField(max_length=255)),
                ('phonenumber', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=255)),
                ('location', models.CharField(max_length=255)),
            ],
        ),
    ]