# Generated by Django 4.2.19 on 2025-03-12 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0007_remove_articleinfo_desc'),
    ]

    operations = [
        migrations.AddField(
            model_name='articleinfo',
            name='desc',
            field=models.TextField(default='description', verbose_name='描述'),
            preserve_default=False,
        ),
    ]
