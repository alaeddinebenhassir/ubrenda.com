# Generated by Django 2.2.2 on 2019-07-18 19:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catloge', '0009_item_brand'),
    ]

    operations = [
        migrations.CreateModel(
            name='sub_cotegorie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('slug', models.SlugField(blank=True, help_text=' unique value for product url created frome name ')),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('meta_keywords', models.CharField(help_text='for meta tags ', max_length=255, verbose_name='Meta Keywords')),
                ('meta_description', models.CharField(help_text='for meta tags ', max_length=255, verbose_name='Meta Description ')),
                ('parent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catloge.Categorie')),
            ],
        ),
    ]