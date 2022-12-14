# Generated by Django 3.2.10 on 2022-09-18 20:13

from django.db import migrations, models
import imagegallery.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32)),
                ('cover', models.ImageField(blank=True, null=True, upload_to=imagegallery.models.upload_path)),
            ],
        ),
        migrations.CreateModel(
            name='StockFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('price', models.IntegerField()),
                ('volume', models.IntegerField()),
                ('info', models.FileField(upload_to='')),
            ],
        ),
    ]
