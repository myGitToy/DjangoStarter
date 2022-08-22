# Generated by Django 3.2.12 on 2022-08-22 11:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_deleted', models.BooleanField(default=False, verbose_name='是否已删除')),
                ('created_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='创建时间')),
                ('updated_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='更新时间')),
                ('name', models.CharField(default='', max_length=200, verbose_name='姓名')),
                ('alias', models.CharField(default='', max_length=200, verbose_name='别名')),
                ('gender', models.CharField(choices=[('male', '男'), ('female', '女'), ('unknown', '未知')], default='unknown', max_length=20, verbose_name='性别')),
                ('phone', models.CharField(default='', max_length=11, verbose_name='手机号')),
                ('user', models.OneToOneField(db_constraint=False, on_delete=django.db.models.deletion.DO_NOTHING, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '用户资料',
                'verbose_name_plural': '用户资料',
                'db_table': 'user_profile',
            },
        ),
    ]
