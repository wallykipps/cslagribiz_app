# Generated by Django 2.0.2 on 2020-06-28 20:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('enterprise', '0005_auto_20200603_0217'),
        ('layers', '0006_layersexpenses_cashpoint'),
    ]

    operations = [
        migrations.CreateModel(
            name='LayersCashDeposit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deposit_date', models.DateField()),
                ('amount', models.DecimalField(decimal_places=0, max_digits=5)),
                ('cashpoint', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='layers.LayersCashPoints', verbose_name='deposit_point')),
                ('enterprise_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='enterprise.EnterpriseType', verbose_name='enterprise_type')),
                ('section', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='layers.LayersSection', verbose_name='section')),
                ('staff', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='enterprise.Staff', verbose_name='depositor')),
            ],
            options={
                'verbose_name_plural': 'Layers Deposit',
                'ordering': ['-deposit_date'],
            },
        ),
    ]
