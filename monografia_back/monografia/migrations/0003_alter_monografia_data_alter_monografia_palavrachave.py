# Generated by Django 4.1.2 on 2022-10-22 22:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monografia', '0002_remove_monografia_nome_alter_monografia_autor_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='monografia',
            name='data',
            field=models.DateField(default='', max_length=30),
        ),
        migrations.AlterField(
            model_name='monografia',
            name='palavrachave',
            field=models.CharField(default='', max_length=100, verbose_name='Palavra-chave'),
        ),
    ]