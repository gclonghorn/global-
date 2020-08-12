# Generated by Django 2.2 on 2020-08-11 20:25

import ckeditor_uploader.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
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
                ('role', models.IntegerField(default=0, verbose_name='文档权限')),
                ('create_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='文档创建者')),
                ('parent_doc', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='child_docs', to='documents.Document', verbose_name='上级文件夹')),
                ('top_doc', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='project_docs', to='documents.Document', verbose_name='团队空间顶级文件夹')),
            ],
            options={
                'verbose_name': '文档',
            },
        ),
    ]
