# Generated by Django 2.0.2 on 2020-06-27 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('layers', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='layerseggslosses',
            options={'ordering': ['stock_date'], 'verbose_name_plural': 'Layers Eggs Losses'},
        ),
        migrations.AddField(
            model_name='layerseggslosses',
            name='eggs_stock_actual',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='layersstockmovement',
            name='birds_stock_actual',
            field=models.IntegerField(blank=True, default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='layersstockmovement',
            name='stock_movement_notes',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='layersstockmovement',
            name='stock_movement_reason',
            field=models.CharField(choices=[('', 'Reason'), ('Day Old Chicks', 'Day Old Chicks'), ('Mortality', 'Mortality'), ('Stolen', 'Stolen'), ('Unaccounted', 'Unaccounted'), ('Error Correction', 'Error Correction')], default='', max_length=15),
        ),
        migrations.AlterField(
            model_name='layersstockmovement',
            name='stock_movement_type',
            field=models.CharField(choices=[('', 'Type of Movement'), ('Stock In', 'Stock In'), ('Stock Out', 'Stock Out')], default='', max_length=15),
        ),
    ]