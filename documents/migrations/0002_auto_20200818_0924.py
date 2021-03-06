# Generated by Django 2.2 on 2020-08-18 09:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('documents', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='create_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='create', to=settings.AUTH_USER_MODEL, verbose_name='文档创建者'),
        ),
        migrations.AddField(
            model_name='document',
            name='editor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='edit', to=settings.AUTH_USER_MODEL, verbose_name='当前编辑者'),
        ),
        migrations.AddField(
            model_name='document',
            name='last_modify_user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='modify', to=settings.AUTH_USER_MODEL, verbose_name='最后修改者'),
        ),
        migrations.AddField(
            model_name='document',
            name='parent_doc',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='child_docs', to='documents.Document', verbose_name='上级文件夹'),
        ),
    ]
