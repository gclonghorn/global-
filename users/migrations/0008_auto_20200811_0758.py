# Generated by Django 2.2 on 2020-08-11 07:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_auto_20200811_0757'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='tel',
            new_name='mobile',
        ),
        migrations.RenameField(
            model_name='verifycode',
            old_name='tel',
            new_name='mobile',
        ),
    ]
