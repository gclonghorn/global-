# Generated by Django 2.2 on 2020-08-16 12:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('documents', '0001_initial'),
        ('comments', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='author',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to=settings.AUTH_USER_MODEL, verbose_name='作者'),
        ),
        migrations.AddField(
            model_name='comment',
            name='document',
            field=models.ForeignKey(default=1, help_text='被评论文章', on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='documents.Document', verbose_name='文章'),
        ),
        migrations.AddField(
            model_name='comment',
            name='reply_comment',
            field=models.ForeignKey(blank=True, help_text='父级评论', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='replies', to='comments.Comment'),
        ),
        migrations.AddField(
            model_name='collect',
            name='author',
            field=models.ForeignKey(default=1, help_text='收藏者', on_delete=django.db.models.deletion.CASCADE, related_name='collects', to=settings.AUTH_USER_MODEL, verbose_name='收藏者'),
        ),
        migrations.AddField(
            model_name='collect',
            name='document',
            field=models.ForeignKey(default=1, help_text='被收藏文章', on_delete=django.db.models.deletion.CASCADE, related_name='collects', to='documents.Document', verbose_name='文章'),
        ),
        migrations.AlterUniqueTogether(
            name='collect',
            unique_together={('author', 'document')},
        ),
    ]