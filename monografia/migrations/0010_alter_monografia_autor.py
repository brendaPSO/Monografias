# Generated by Django 4.1.2 on 2022-11-16 21:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20221113_1247'),
        ('monografia', '0009_alter_monografia_autor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='monografia',
            name='autor',
            field=models.OneToOneField(limit_choices_to={'autor': True}, on_delete=django.db.models.deletion.CASCADE, to='core.pessoa'),
        ),
    ]
