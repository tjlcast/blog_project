# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-24 09:07
from __future__ import unicode_literals

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.ASCIIUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=30, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('avatar', models.ImageField(blank=True, max_length=200, null=True, upload_to=b'avatar/%Y/%m', verbose_name=b'\xe7\x94\xa8\xe6\x88\xb7\xe5\xa4\xb4\xe5\x83\x8f')),
                ('qq', models.CharField(blank=True, max_length=20, null=True, verbose_name=b'QQ\xe5\x8f\xb7\xe7\xa0\x81')),
                ('mobile', models.CharField(blank=True, max_length=11, null=True, unique=True, verbose_name=b'\xe6\x89\x8b\xe6\x9c\xba\xe5\x8f\xb7\xe7\xa0\x81')),
                ('url', models.URLField(blank=True, max_length=100, null=True, verbose_name=b'\xe4\xb8\xaa\xe4\xba\xba\xe7\xbd\x91\xe9\xa1\xb5\xe5\x9c\xb0\xe5\x9d\x80')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'ordering': ['-id'],
                'verbose_name': '\u7528\u6237',
                'verbose_name_plural': '\u7528\u6237',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Ad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name=b'\xe5\xb9\xbf\xe5\x91\x8a\xe6\xa0\x87\xe9\xa2\x98')),
                ('description', models.CharField(max_length=200, verbose_name=b'\xe5\xb9\xbf\xe5\x91\x8a\xe6\x8f\x8f\xe8\xbf\xb0')),
                ('image_url', models.ImageField(upload_to=b'ad/%Y/%m', verbose_name=b'\xe5\x9b\xbe\xe7\x89\x87\xe8\xb7\xaf\xe5\xbe\x84')),
                ('callback_url', models.URLField(blank=True, null=True, verbose_name=b'\xe5\x9b\x9e\xe8\xb0\x83url')),
                ('date_publish', models.DateTimeField(auto_now_add=True, verbose_name=b'\xe5\x8f\x91\xe5\xb8\x83\xe6\x97\xb6\xe9\x97\xb4')),
                ('index', models.IntegerField(default=999, verbose_name=b'\xe6\x8e\x92\xe5\x88\x97\xe9\xa1\xba\xe5\xba\x8f(\xe4\xbb\x8e\xe5\xb0\x8f\xe5\x88\xb0\xe5\xa4\xa7)')),
            ],
            options={
                'ordering': ['index', 'id'],
                'verbose_name': '\u5e7f\u544a',
                'verbose_name_plural': '\u5e7f\u544a',
            },
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name=b'\xe6\x96\x87\xe7\xab\xa0\xe6\xa0\x87\xe9\xa2\x98')),
                ('desc', models.CharField(max_length=50, verbose_name=b'\xe6\x96\x87\xe7\xab\xa0\xe6\x8f\x8f\xe8\xbf\xb0')),
                ('content', models.TextField(verbose_name=b'\xe6\x96\x87\xe7\xab\xa0\xe5\x86\x85\xe5\xae\xb9')),
                ('click_count', models.IntegerField(default=0, verbose_name=b'\xe7\x82\xb9\xe5\x87\xbb\xe6\xac\xa1\xe6\x95\xb0')),
                ('is_recommend', models.BooleanField(default=False, verbose_name=b'\xe6\x98\xaf\xe5\x90\xa6\xe6\x8e\xa8\xe8\x8d\x90')),
                ('date_publish', models.DateTimeField(auto_now_add=True, verbose_name=b'\xe5\x8f\x91\xe5\xb8\x83\xe6\x97\xb6\xe9\x97\xb4')),
            ],
            options={
                'ordering': ['-date_publish'],
                'verbose_name': '\u6587\u7ae0',
                'verbose_name_plural': '\u6587\u7ae0',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name=b'\xe5\x88\x86\xe7\xb1\xbb\xe5\x90\x8d\xe7\xa7\xb0')),
                ('index', models.IntegerField(default=999, verbose_name=b'\xe5\x88\x86\xe7\xb1\xbb\xe7\x9a\x84\xe6\x8e\x92\xe5\xba\x8f')),
            ],
            options={
                'ordering': ['index', 'id'],
                'verbose_name': '\u5206\u7c7b',
                'verbose_name_plural': '\u5206\u7c7b',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(verbose_name=b'\xe8\xaf\x84\xe8\xae\xba\xe5\x86\x85\xe5\xae\xb9')),
                ('username', models.CharField(blank=True, max_length=30, null=True, verbose_name=b'\xe7\x94\xa8\xe6\x88\xb7\xe5\x90\x8d')),
                ('email', models.EmailField(blank=True, max_length=50, null=True, verbose_name=b'\xe9\x82\xae\xe7\xae\xb1\xe5\x9c\xb0\xe5\x9d\x80')),
                ('url', models.URLField(blank=True, max_length=100, null=True, verbose_name=b'\xe4\xb8\xaa\xe4\xba\xba\xe7\xbd\x91\xe9\xa1\xb5\xe5\x9c\xb0\xe5\x9d\x80')),
                ('date_publish', models.DateTimeField(auto_now_add=True, verbose_name=b'\xe5\x8f\x91\xe5\xb8\x83\xe6\x97\xb6\xe9\x97\xb4')),
                ('article', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.Article', verbose_name=b'\xe6\x96\x87\xe7\xab\xa0')),
                ('pid', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.Comment', verbose_name=b'\xe7\x88\xb6\xe7\xba\xa7\xe8\xaf\x84\xe8\xae\xba')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name=b'\xe7\x94\xa8\xe6\x88\xb7')),
            ],
            options={
                'verbose_name': '\u8bc4\u8bba',
                'verbose_name_plural': '\u8bc4\u8bba',
            },
        ),
        migrations.CreateModel(
            name='Links',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name=b'\xe6\xa0\x87\xe9\xa2\x98')),
                ('description', models.CharField(max_length=200, verbose_name=b'\xe5\x8f\x8b\xe6\x83\x85\xe9\x93\xbe\xe6\x8e\xa5\xe6\x8f\x8f\xe8\xbf\xb0')),
                ('callback_url', models.URLField(verbose_name=b'url\xe5\x9c\xb0\xe5\x9d\x80')),
                ('date_publish', models.DateTimeField(auto_now_add=True, verbose_name=b'\xe5\x8f\x91\xe5\xb8\x83\xe6\x97\xb6\xe9\x97\xb4')),
                ('index', models.IntegerField(default=999, verbose_name=b'\xe6\x8e\x92\xe5\x88\x97\xe9\xa1\xba\xe5\xba\x8f(\xe4\xbb\x8e\xe5\xb0\x8f\xe5\x88\xb0\xe5\xa4\xa7)')),
            ],
            options={
                'ordering': ['index', 'id'],
                'verbose_name': '\u53cb\u60c5\u94fe\u63a5',
                'verbose_name_plural': '\u53cb\u60c5\u94fe\u63a5',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name=b'\xe6\xa0\x87\xe7\xad\xbe\xe5\x90\x8d\xe7\xa7\xb0')),
            ],
            options={
                'verbose_name': '\u6807\u7b7e',
                'verbose_name_plural': '\u6807\u7b7e',
            },
        ),
        migrations.AddField(
            model_name='article',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.Category', verbose_name=b'\xe5\x88\x86\xe7\xb1\xbb'),
        ),
        migrations.AddField(
            model_name='article',
            name='tag',
            field=models.ManyToManyField(to='blog.Tag', verbose_name=b'\xe6\xa0\x87\xe7\xad\xbe'),
        ),
        migrations.AddField(
            model_name='article',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name=b'\xe7\x94\xa8\xe6\x88\xb7'),
        ),
    ]
