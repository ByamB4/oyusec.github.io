# Generated by Django 3.1.7 on 2021-04-26 08:43

import apps.core.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Academy',
            fields=[
                ('uuid', apps.core.models.UUIDField(blank=True, editable=False, max_length=32, primary_key=True, serialize=False, unique=True)),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Created date')),
                ('last_updated_date', models.DateTimeField(auto_now=True, verbose_name='Last updated date')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='Name')),
                ('description', models.TextField(default='CTF', verbose_name='Description')),
                ('status', models.CharField(choices=[('coming', 'coming'), ('archive', 'archive'), ('live', 'live')], default='live', max_length=100, verbose_name='Status')),
                ('slug', models.SlugField(unique=True)),
                ('photo', models.URLField(blank=True, default='https://github.com/OyuTech/Utils/blob/main/oyusec/oyusec.png', null=True)),
                ('category', models.CharField(choices=[('Capture The Flag', 'Capture The Flag'), ('Сүлжээний аюулгүй байдал', 'Сүлжээний аюулгүй байдал'), ('Веб аюулгүй байдал', 'Веб аюулгүй байдал'), ('Аюулгүй кодчилол', 'Аюулгүй кодчилол')], default='Capture The Flag', max_length=100, verbose_name='Category')),
            ],
            options={
                'verbose_name': 'Academy',
            },
        ),
        migrations.CreateModel(
            name='AcademyUser',
            fields=[
                ('uuid', apps.core.models.UUIDField(blank=True, editable=False, max_length=32, primary_key=True, serialize=False, unique=True)),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Created date')),
                ('last_updated_date', models.DateTimeField(auto_now=True, verbose_name='Last updated date')),
            ],
            options={
                'verbose_name': 'Academy User',
            },
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('uuid', apps.core.models.UUIDField(blank=True, editable=False, max_length=32, primary_key=True, serialize=False, unique=True)),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Created date')),
                ('last_updated_date', models.DateTimeField(auto_now=True, verbose_name='Last updated date')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('content', models.TextField(blank=True, null=True, verbose_name='Content')),
                ('question', models.CharField(blank=True, max_length=100, null=True, verbose_name='Question')),
                ('answer', models.CharField(blank=True, max_length=100, null=True, verbose_name='Answer')),
                ('point', models.PositiveIntegerField(default=0, verbose_name='Point')),
                ('hint', models.CharField(blank=True, max_length=100, null=True, verbose_name='Hint')),
            ],
            options={
                'verbose_name': 'Section',
            },
        ),
        migrations.CreateModel(
            name='SectionUser',
            fields=[
                ('uuid', apps.core.models.UUIDField(blank=True, editable=False, max_length=32, primary_key=True, serialize=False, unique=True)),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Created date')),
                ('last_updated_date', models.DateTimeField(auto_now=True, verbose_name='Last updated date')),
                ('is_completed', models.BooleanField(default=False)),
                ('section', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academy.section')),
            ],
            options={
                'verbose_name': 'Section User',
            },
        ),
    ]
