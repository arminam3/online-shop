# Generated by Django 4.1 on 2022-08-28 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='age',
            field=models.IntegerField(null=True, verbose_name='سن'),
        ),
    ]