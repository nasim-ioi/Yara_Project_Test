# Generated by Django 2.2 on 2020-03-28 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='is_owner',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]