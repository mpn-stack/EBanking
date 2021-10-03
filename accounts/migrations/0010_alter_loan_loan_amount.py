# Generated by Django 3.2.7 on 2021-10-02 19:13

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_auto_20211002_2241'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loan',
            name='loan_amount',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=11, validators=[django.core.validators.MinValueValidator(1000000), django.core.validators.MaxValueValidator(100000000)]),
        ),
    ]
