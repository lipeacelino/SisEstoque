# Generated by Django 2.1.1 on 2018-10-12 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produtos', '0002_auto_20181012_1453'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='produto',
            name='id',
        ),
        migrations.AlterField(
            model_name='produto',
            name='codigo',
            field=models.CharField(max_length=10, primary_key=True, serialize=False),
        ),
    ]
