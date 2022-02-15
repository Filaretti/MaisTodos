# Generated by Django 4.0.2 on 2022-02-14 01:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cashback', '0003_purchase_product_purchase'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='calculated_cashback',
            field=models.FloatField(blank=True, help_text='Total calculado do cashback formula: (total_value * (type.percentage_cashback / 100))', null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='customer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='cashback.customer'),
        ),
        migrations.AddField(
            model_name='product',
            name='total_value',
            field=models.FloatField(blank=True, help_text='Total calculado do value * qty', null=True),
        ),
    ]