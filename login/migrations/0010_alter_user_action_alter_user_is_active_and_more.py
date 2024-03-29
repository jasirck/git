# Generated by Django 5.0 on 2024-01-06 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0009_alter_user_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='action',
            field=models.CharField(default='active', max_length=10),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_superuser',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=10),
        ),
    ]
