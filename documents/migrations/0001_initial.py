# Generated by Django 2.2 on 2020-08-18 09:24

import ckeditor_uploader.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='文档标题')),
                ('content', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='文档内容')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='文档创建时间')),
                ('modify_time', models.DateTimeField(auto_now=True, verbose_name='文档修改时间')),
                ('type', models.IntegerField(default=0, verbose_name='是否文件夹')),
                ('status', models.IntegerField(default=1, verbose_name='文档状态')),
                ('role', models.IntegerField(default=0, verbose_name='0完全公开1团队公开2团队读写3团队只读')),
                ('thumbnail', models.ImageField(blank=True, help_text='缩略图', null=True, upload_to='upload', verbose_name='缩略图')),
                ('create_by_model', models.ForeignKey(blank=True, help_text='模板', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='model', to='documents.Document', verbose_name='文档模板')),
            ],
            options={
                'verbose_name': '文档',
            },
        ),
    ]
