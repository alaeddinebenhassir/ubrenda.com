# Generated by Django 2.2.2 on 2019-07-03 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catloge', '0004_auto_20190703_1237'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='descreption',
            field=models.TextField(),
        ),
    ]
