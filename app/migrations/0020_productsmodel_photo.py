# Generated by Django 3.0.2 on 2020-04-04 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0019_usersdetailsmodel_balance'),
    ]

    operations = [
        migrations.AddField(
            model_name='productsmodel',
            name='photo',
            field=models.ImageField(default=False, upload_to='products/'),
        ),
    ]
