# Generated by Django 4.2.3 on 2023-07-28 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0008_alter_buy_ph'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buy',
            name='dob',
            field=models.DateTimeField(),
        ),
    ]
