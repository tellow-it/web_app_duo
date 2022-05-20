# Generated by Django 4.0.3 on 2022-05-20 15:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0005_alter_post_likes'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='author_en',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='blog_posts', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='post',
            name='author_ru',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='blog_posts', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='post',
            name='content_en',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='content_ru',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='created_on_en',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='created_on_ru',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='title_en',
            field=models.CharField(max_length=200, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='post',
            name='title_ru',
            field=models.CharField(max_length=200, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='post',
            name='updated_on_en',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='updated_on_ru',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
