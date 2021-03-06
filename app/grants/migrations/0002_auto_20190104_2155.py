# Generated by Django 2.1.2 on 2019-01-04 21:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grants', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscription',
            name='amount_per_period',
            field=models.DecimalField(decimal_places=18, default=1, help_text='The promised contribution amount per period.', max_digits=64),
        ),
    ]
