# Generated by Django 2.2 on 2020-08-15 11:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('documents', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(auto_now_add=True, verbose_name='消息发送时间')),
                ('type', models.IntegerField(default=0, verbose_name='消息类型')),
                ('status', models.IntegerField(default=0, verbose_name='文档状态')),
                ('document', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='documents.Document', verbose_name='消息关联的文档/团队')),
            ],
            options={
                'verbose_name': '消息',
            },
        ),
    ]