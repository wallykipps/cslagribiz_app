# Generated by Django 2.0.2 on 2020-06-27 16:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('enterprise', '0005_auto_20200603_0217'),
        ('layers', '0003_auto_20200627_1934'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='LayersEggsLosses',
            new_name='LayersEggsInventory',
        ),
        migrations.AlterModelOptions(
            name='layerseggsinventory',
            options={'ordering': ['stock_date'], 'verbose_name_plural': 'Layers Eggs Inventory'},
        ),
    ]