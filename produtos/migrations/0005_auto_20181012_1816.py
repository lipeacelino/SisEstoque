# Generated by Django 2.1.1 on 2018-10-12 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produtos', '0004_auto_20181012_1803'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='preco',
            field=models.DecimalField(decimal_places=2, max_digits=6),
        ),
    ]
