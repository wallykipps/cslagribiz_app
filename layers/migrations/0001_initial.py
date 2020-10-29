# Generated by Django 2.0.2 on 2020-06-21 18:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('enterprise', '0005_auto_20200603_0217'),
    ]

    operations = [
        migrations.CreateModel(
            name='LayersCostCategories',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cost_category', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name_plural': 'Layers Cost Categories',
            },
        ),
        migrations.CreateModel(
            name='LayersCustomers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reg_date', models.DateField()),
                ('firstname', models.CharField(max_length=255)),
                ('lastname', models.CharField(max_length=255)),
                ('phonenumber', models.CharField(max_length=10)),
                ('email', models.EmailField(blank=True, max_length=255, null=True)),
                ('location', models.CharField(blank=True, max_length=255)),
            ],
            options={
                'verbose_name_plural': 'Layers Customers',
                'db_table': 'layers_layerscustomers',
                'ordering': ['-reg_date'],
            },
        ),
        migrations.CreateModel(
            name='LayersEggsLosses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stock_date', models.DateField()),
                ('unit', models.CharField(choices=[('CRATES', 'Crates'), ('PIECES', 'Pieces')], default='PIECES', max_length=15)),
                ('loss_type', models.CharField(choices=[('DEFECTS', 'Defects'), ('BREAKAGES', 'Breakages'), ('EXPIRED', 'Expired'), ('UNACCOUNTED', 'Unaccounted')], default='DEFECTS', max_length=15)),
                ('quantity_lost', models.IntegerField()),
                ('enterprise_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='enterprise.EnterpriseType', verbose_name='enterprise_type')),
            ],
            options={
                'verbose_name_plural': 'Layers Eggs Losses',
                'ordering': ['-stock_date'],
            },
        ),
        migrations.CreateModel(
            name='LayersExpenses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('purchase_date', models.DateField()),
                ('expense_details', models.CharField(max_length=255)),
                ('quantity', models.DecimalField(decimal_places=0, max_digits=5)),
                ('unitprice', models.DecimalField(decimal_places=2, max_digits=10)),
                ('cost_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='layers.LayersCostCategories', verbose_name='cost category')),
                ('enterprise_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='enterprise.EnterpriseType', verbose_name='enterprise_type')),
                ('paymentmode', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='enterprise.PaymentModes', verbose_name='payment_mode')),
            ],
            options={
                'verbose_name_plural': 'Layers Expenses',
                'ordering': ['-purchase_date'],
            },
        ),
        migrations.CreateModel(
            name='LayersProduction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prod_date', models.DateField()),
                ('gross', models.IntegerField()),
                ('defects', models.IntegerField()),
                ('broken', models.IntegerField()),
                ('enterprise_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='enterprise.EnterpriseType', verbose_name='enterprise_type')),
            ],
            options={
                'verbose_name_plural': 'Layers Production',
                'ordering': ['-prod_date'],
            },
        ),
        migrations.CreateModel(
            name='LayersProducts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.CharField(max_length=255)),
                ('unit_measure', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name_plural': 'Layers Products',
            },
        ),
        migrations.CreateModel(
            name='LayersSales',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('quantity', models.IntegerField()),
                ('unitprice', models.DecimalField(decimal_places=2, max_digits=5)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='layers.LayersCustomers', verbose_name='customer')),
                ('enterprise_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Layers', to='enterprise.EnterpriseType', verbose_name='enterprise_type')),
                ('paymentmode', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='enterprise.PaymentModes', verbose_name='payment_mode')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='layers.LayersProducts', verbose_name='product')),
            ],
            options={
                'verbose_name_plural': 'Layers Sales',
                'ordering': ['-date'],
            },
        ),
        migrations.CreateModel(
            name='LayersSection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('section', models.CharField(max_length=255)),
                ('sub_section', models.CharField(blank=True, max_length=255, null=True)),
                ('sub_sub_section', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'verbose_name_plural': 'Layers Units',
            },
        ),
        migrations.CreateModel(
            name='LayersStockMovement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stock_date', models.DateField()),
                ('stock_movement_type', models.CharField(choices=[('Stock In', 'Stock In'), ('Stock Out', 'Stock Out')], default='Stock out', max_length=15)),
                ('stock_movement_reason', models.CharField(choices=[('Day Old Chicks', 'Day Old Chicks'), ('Mortality', 'Mortality'), ('Stolen', 'Stolen'), ('Unaccounted', 'Unaccounted')], default='Mortality', max_length=15)),
                ('birds', models.IntegerField()),
                ('birds_stock_actual', models.IntegerField(null=True)),
                ('stock_movement_notes', models.CharField(max_length=255)),
                ('enterprise_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='enterprise.EnterpriseType', verbose_name='enterprise_type')),
                ('section', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='layers.LayersSection', verbose_name='section')),
                ('staff', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='enterprise.Staff', verbose_name='staff')),
            ],
            options={
                'verbose_name_plural': 'Layers Birds Inventory',
                'ordering': ['stock_date'],
            },
        ),
        migrations.CreateModel(
            name='LayersVendors',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vendor_date', models.DateField()),
                ('vendor', models.CharField(blank=True, max_length=255, null=True)),
                ('phonenumber', models.CharField(blank=True, max_length=10, null=True)),
                ('email', models.EmailField(blank=True, max_length=255, null=True)),
                ('location', models.CharField(blank=True, max_length=255)),
            ],
            options={
                'verbose_name_plural': 'Layers Vendors',
                'ordering': ['-vendor_date'],
            },
        ),
        migrations.AddField(
            model_name='layerssales',
            name='section',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='layers.LayersSection', verbose_name='section'),
        ),
        migrations.AddField(
            model_name='layerssales',
            name='staff',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='enterprise.Staff', verbose_name='staff'),
        ),
        migrations.AddField(
            model_name='layersproduction',
            name='section',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='layers.LayersSection', verbose_name='section'),
        ),
        migrations.AddField(
            model_name='layersproduction',
            name='staff',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='enterprise.Staff', verbose_name='staff'),
        ),
        migrations.AddField(
            model_name='layersexpenses',
            name='section',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='layers.LayersSection', verbose_name='section'),
        ),
        migrations.AddField(
            model_name='layersexpenses',
            name='staff',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='enterprise.Staff', verbose_name='purchaser'),
        ),
        migrations.AddField(
            model_name='layersexpenses',
            name='vendor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='layers.LayersVendors', verbose_name='vendor'),
        ),
        migrations.AddField(
            model_name='layerseggslosses',
            name='section',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='layers.LayersSection', verbose_name='section'),
        ),
        migrations.AddField(
            model_name='layerseggslosses',
            name='staff',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='enterprise.Staff', verbose_name='staff'),
        ),
    ]
