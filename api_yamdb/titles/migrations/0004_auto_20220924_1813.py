# Generated by Django 2.2.16 on 2022-09-24 15:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('titles', '0003_auto_20220924_1733'),
    ]

    operations = [
        migrations.AlterField(
            model_name='title',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='titles', to='titles.Category', verbose_name='Категория'),
        ),
    ]
