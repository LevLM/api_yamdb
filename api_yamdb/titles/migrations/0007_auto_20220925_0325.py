# Generated by Django 2.2.16 on 2022-09-25 00:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('titles', '0006_auto_20220925_0325'),
    ]

    operations = [
        migrations.AlterField(
            model_name='title',
            name='genre',
            field=models.ManyToManyField(to='titles.Genre', verbose_name='Жанр'),
        ),
    ]