# Generated by Django 2.2.16 on 2022-09-25 22:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('titles', '0013_auto_20220926_0111'),
    ]

    operations = [
        migrations.AlterField(
            model_name='title',
            name='rating',
            field=models.IntegerField(default=None, null=True),
        ),
    ]