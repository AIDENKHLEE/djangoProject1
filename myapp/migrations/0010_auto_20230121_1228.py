# Generated by Django 3.2.16 on 2023-01-21 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0009_alter_accountholder_age'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accountholder',
            name='age',
            field=models.IntegerField(default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='user',
            name='age',
            field=models.IntegerField(default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.CharField(default='', max_length=20),
        ),
    ]
