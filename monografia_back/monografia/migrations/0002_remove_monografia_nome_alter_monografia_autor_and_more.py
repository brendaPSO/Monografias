# Generated by Django 4.1.2 on 2022-10-22 22:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monografia', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='monografia',
            name='nome',
        ),
        migrations.AlterField(
            model_name='monografia',
            name='autor',
            field=models.CharField(default='', max_length=80),
        ),
        migrations.AlterField(
            model_name='monografia',
            name='coorientador',
            field=models.CharField(default='', max_length=80),
        ),
        migrations.AlterField(
            model_name='monografia',
            name='curso',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='monografia',
            name='link',
            field=models.CharField(default='', max_length=512, verbose_name='Link para PDF'),
        ),
        migrations.AlterField(
            model_name='monografia',
            name='orientador',
            field=models.CharField(default='', max_length=80),
        ),
        migrations.AlterField(
            model_name='monografia',
            name='resumo',
            field=models.TextField(default='', max_length=3200),
        ),
        migrations.AlterField(
            model_name='monografia',
            name='titulo',
            field=models.CharField(default='', max_length=256),
        ),
        migrations.AlterField(
            model_name='monografia',
            name='universidade',
            field=models.CharField(default='', max_length=128),
        ),
    ]
