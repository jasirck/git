# Generated by Django 5.0 on 2024-01-01 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='password',
            field=models.IntegerField(default=1234, verbose_name=''),
            preserve_default=False,
        ),
    ]
