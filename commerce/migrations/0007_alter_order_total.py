# Generated by Django 3.2.9 on 2021-12-24 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commerce', '0006_auto_20211221_0844'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='total',
            field=models.DecimalField(blank=True, decimal_places=0, default=0, max_digits=1000, null=True, verbose_name='total'),
        ),
    ]
