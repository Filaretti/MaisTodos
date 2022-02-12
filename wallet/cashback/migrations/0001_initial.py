# Generated by Django 4.0.2 on 2022-02-12 02:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('document', models.CharField(help_text='CPF do customer', max_length=15)),
                ('name', models.CharField(help_text='Nome do customer', max_length=100)),
            ],
        ),
    ]
