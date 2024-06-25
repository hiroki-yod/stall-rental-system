# Generated by Django 5.0 on 2024-06-25 12:57

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='団体名')),
                ('name_kana', models.CharField(max_length=64, verbose_name='団体名（カナ）')),
                ('representative_name', models.CharField(max_length=64, verbose_name='代表者氏名')),
                ('representative_email', models.EmailField(max_length=254, verbose_name='代表者メールアドレス')),
                ('representative_phone_number', models.CharField(max_length=32, verbose_name='代表者電話番号')),
                ('group_type', models.CharField(choices=[('COMPANY', '企業'), ('NPO', 'NPO法人'), ('VOLUNTARY', 'ボランティア団体'), ('OTHER', 'その他')], max_length=16, verbose_name='団体種類')),
                ('purpose', models.TextField(verbose_name='活動目的')),
                ('activities', models.TextField(verbose_name='活動内容')),
                ('members', models.ManyToManyField(related_name='member_groups', to=settings.AUTH_USER_MODEL, verbose_name='メンバー')),
            ],
            options={
                'verbose_name': '団体',
                'db_table': 'group',
            },
        ),
    ]
