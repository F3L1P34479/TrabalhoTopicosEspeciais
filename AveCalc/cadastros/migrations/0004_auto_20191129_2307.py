# Generated by Django 2.1.7 on 2019-11-30 01:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastros', '0003_auto_20191129_2149'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entrada',
            name='peso',
            field=models.PositiveIntegerField(),
        ),
    ]
