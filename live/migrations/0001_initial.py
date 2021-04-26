# Generated by Django 3.1.5 on 2021-04-10 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('so_line', models.CharField(max_length=14)),
                ('customer_no', models.CharField(max_length=15)),
                ('sales_order_no', models.CharField(max_length=7)),
                ('customer_name', models.CharField(max_length=50)),
                ('linekey', models.CharField(max_length=6)),
                ('item_code', models.CharField(max_length=30)),
                ('item_cod_desc', models.CharField(max_length=64)),
                ('so_header', models.DateField()),
                ('prom_date', models.DateField()),
                ('clear_date', models.DateField()),
                ('exp_date_i', models.DateField()),
                ('exp_date_f', models.DateField()),
                ('qty', models.IntegerField()),
                ('qty_shipped', models.IntegerField()),
                ('unit_price', models.CharField(default='0', max_length=20)),
                ('production_notes', models.CharField(max_length=512)),
                ('qty_on_hand', models.IntegerField()),
                ('rma_number', models.IntegerField()),
                ('drop_ship', models.CharField(max_length=2)),
                ('comments', models.CharField(max_length=512)),
                ('active', models.BooleanField(default=1)),
                ('notes', models.CharField(blank=True, max_length=512)),
                ('status', models.CharField(choices=[('NEW', 'NEW'), ('KTG', 'KITTING'), ('WTN', 'WAITING'), ('KTD', 'KITTED'), ('TST', 'FCT in PROGRESS'), ('OHL', 'ON HOLD'), ('BLD', 'Mech Assy'), ('PSS', 'FCT PASSED'), ('BRI', 'BURN-IN'), ('QAA', 'QA'), ('SHP', 'SHIPPING'), ('NAN', 'NA')], default='NEW', max_length=3)),
                ('profile', models.CharField(choices=[('P0', 'QA'), ('P1', 'FCT -> QA'), ('P2', 'FCT -> Burn In -> QA'), ('P3', 'FCT -> Production -> Burn In -> QA'), ('P4', 'Production -> Burn In -> QA'), ('P9', 'NA')], default='P0', max_length=2)),
            ],
            options={
                'ordering': ('exp_date_f',),
            },
        ),
    ]
