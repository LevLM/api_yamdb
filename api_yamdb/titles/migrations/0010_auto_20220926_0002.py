# Generated by Django 2.2.16 on 2022-09-25 21:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('titles', '0009_auto_20220925_1631'),
    ]

    operations = [
        migrations.AlterField(
            model_name='title',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='titles_category', to='titles.Category', verbose_name='Категория'),
        ),
        migrations.AlterField(
            model_name='title',
            name='genre',
            field=models.ManyToManyField(blank=True, to='titles.Genre', verbose_name='Жанр'),
        ),
    ]
