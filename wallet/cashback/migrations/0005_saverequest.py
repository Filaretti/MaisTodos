# Generated by Django 3.2.9 on 2022-02-23 23:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cashback', '0004_product_calculated_cashback_product_customer_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='SaveRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('received_api', models.TextField(blank=True, null=True)),
                ('response_api_maistodos', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
