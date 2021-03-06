# Generated by Django 3.0.2 on 2020-04-01 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0017_auto_20200401_1354'),
    ]

    operations = [
        migrations.AddField(
            model_name='camerasmodel',
            name='category',
            field=models.CharField(choices=[('Mobiles', 'Mobiles'), ('Laptops', 'Laptops'), ('Cameras', 'Cameras'), ('Tvs', 'Tvs')], default=False, max_length=30),
        ),
        migrations.AddField(
            model_name='laptopsmodel',
            name='category',
            field=models.CharField(choices=[('Mobiles', 'Mobiles'), ('Laptops', 'Laptops'), ('Cameras', 'Cameras'), ('Tvs', 'Tvs')], default=False, max_length=30),
        ),
        migrations.AddField(
            model_name='mobilesmodel',
            name='category',
            field=models.CharField(choices=[('Mobiles', 'Mobiles'), ('Laptops', 'Laptops'), ('Cameras', 'Cameras'), ('Tvs', 'Tvs')], default=False, max_length=30),
        ),
        migrations.AddField(
            model_name='telivisionsmodel',
            name='category',
            field=models.CharField(choices=[('Mobiles', 'Mobiles'), ('Laptops', 'Laptops'), ('Cameras', 'Cameras'), ('Tvs', 'Tvs')], default=False, max_length=30),
        ),
        migrations.AlterField(
            model_name='ordersmodel',
            name='city',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='ordersmodel',
            name='loaclity',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='ordersmodel',
            name='photo',
            field=models.ImageField(upload_to='telivisions/'),
        ),
        migrations.AlterField(
            model_name='ordersmodel',
            name='product_name',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='ordersmodel',
            name='state',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='savedcardsmodel',
            name='expiry_mm',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='savedcardsmodel',
            name='expiry_yy',
            field=models.IntegerField(),
        ),
    ]
