# Generated by Django 2.2 on 2020-08-18 09:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('documents', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RecycleBin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('delete_time', models.DateTimeField(auto_now_add=True, verbose_name='文档删除时间')),
                ('document', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='documents.Document', verbose_name='被删除文档')),
            ],
            options={
                'verbose_name': '删除记录',
            },
        ),
    ]