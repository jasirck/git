# Generated by Django 5.0 on 2024-01-05 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0006_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='number',
            field=models.IntegerField(max_length=10),
        ),
    ]
