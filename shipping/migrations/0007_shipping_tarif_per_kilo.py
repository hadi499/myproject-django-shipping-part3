# Generated by Django 4.0.4 on 2022-05-12 05:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shipping', '0006_tarifperkilo_updated_alter_shipping_created_at_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='shipping',
            name='tarif_per_kilo',
            field=models.IntegerField(null=True),
        ),
    ]
