# Generated by Django 4.0.6 on 2022-10-10 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wallet', '0005_alter_account_id_alter_card_id_alter_currency_id_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transaction',
            name='transaction_charge',
        ),
        migrations.AlterField(
            model_name='transaction',
            name='transaction_type',
            field=models.CharField(max_length=5, null=True),
        ),
    ]
