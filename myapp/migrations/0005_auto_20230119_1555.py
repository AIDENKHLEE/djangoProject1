# Generated by Django 3.2.16 on 2023-01-19 20:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_auto_20230119_1531'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='partner_attribute',
        ),
        migrations.RemoveField(
            model_name='user',
            name='self_attribute',
        ),
    ]
