# Generated by Django 4.1.5 on 2023-01-09 05:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kStore', '0003_alter_producttable_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producttable',
            name='image',
            field=models.ImageField(upload_to='kStore/static/images/'),
        ),
    ]