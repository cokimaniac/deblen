# Generated by Django 2.2 on 2020-10-04 04:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('debtors', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ammount',
            name='monthly_interest',
            field=models.IntegerField(default=0, verbose_name='Monthly interest ammount of money'),
        ),
        migrations.AddField(
            model_name='ammount',
            name='payment_months',
            field=models.IntegerField(default=1, verbose_name='Months will take debtor to pay full ammount of money'),
        ),
    ]