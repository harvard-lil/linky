# Generated by Django 2.2.16 on 2021-01-28 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perma', '0063_auto_20201008_1907'),
    ]

    operations = [
        migrations.AddField(
            model_name='folder',
            name='cached_path',
            field=models.TextField(blank=True, null=True),
        ),
    ]
