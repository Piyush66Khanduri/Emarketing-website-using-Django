# Generated by Django 4.2.3 on 2023-07-24 02:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0003_alter_sell_pd'),
    ]

    operations = [
        migrations.AddField(
            model_name='sell',
            name='cnt',
            field=models.IntegerField(default=10),
        ),
    ]
