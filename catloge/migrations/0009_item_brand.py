# Generated by Django 2.2.3 on 2019-07-06 22:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catloge', '0008_auto_20190706_2011'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='brand',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
