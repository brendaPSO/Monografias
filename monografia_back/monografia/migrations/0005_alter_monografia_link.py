# Generated by Django 3.2.16 on 2022-11-15 01:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monografia', '0004_auto_20221113_1247'),
    ]

    operations = [
        migrations.AlterField(
            model_name='monografia',
            name='link',
            field=models.URLField(default='', max_length=512, verbose_name='Link para PDF'),
        ),
    ]
