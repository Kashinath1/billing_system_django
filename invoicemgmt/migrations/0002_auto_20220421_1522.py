# Generated by Django 3.2.13 on 2022-04-21 09:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('invoicemgmt', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='invoice',
            name='line_five',
        ),
        migrations.RemoveField(
            model_name='invoice',
            name='line_five_quantity',
        ),
        migrations.RemoveField(
            model_name='invoice',
            name='line_five_total_price',
        ),
        migrations.RemoveField(
            model_name='invoice',
            name='line_five_unit_price',
        ),
        migrations.RemoveField(
            model_name='invoice',
            name='line_four',
        ),
        migrations.RemoveField(
            model_name='invoice',
            name='line_four_quantity',
        ),
        migrations.RemoveField(
            model_name='invoice',
            name='line_four_total_price',
        ),
        migrations.RemoveField(
            model_name='invoice',
            name='line_four_unit_price',
        ),
        migrations.RemoveField(
            model_name='invoice',
            name='line_three',
        ),
        migrations.RemoveField(
            model_name='invoice',
            name='line_three_quantity',
        ),
        migrations.RemoveField(
            model_name='invoice',
            name='line_three_total_price',
        ),
        migrations.RemoveField(
            model_name='invoice',
            name='line_three_unit_price',
        ),
        migrations.RemoveField(
            model_name='invoice',
            name='line_two',
        ),
        migrations.RemoveField(
            model_name='invoice',
            name='line_two_quantity',
        ),
        migrations.RemoveField(
            model_name='invoice',
            name='line_two_total_price',
        ),
        migrations.RemoveField(
            model_name='invoice',
            name='line_two_unit_price',
        ),
    ]
