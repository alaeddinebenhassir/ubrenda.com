# Generated by Django 2.2.2 on 2019-07-05 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catloge', '0006_auto_20190705_1341'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='img',
            field=models.ImageField(default='pic_folder/None/no-img.jpg', upload_to='img/product/'),
        ),
    ]