# Generated by Django 4.0.4 on 2022-05-24 16:24

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('truesync', '0002_added_category_model'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=100)),
                ('slug', models.SlugField(unique=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('is_active', models.BooleanField(db_index=True, default=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('objectives', django.contrib.postgres.fields.ArrayField(base_field=models.TextField(), blank=True, null=True, size=None)),
                ('requirements', django.contrib.postgres.fields.ArrayField(base_field=models.TextField(), blank=True, null=True, size=None)),
                ('thumbnail', models.CharField(blank=True, max_length=200, null=True)),
                ('preview', models.CharField(blank=True, max_length=200, null=True)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='category_courses', to='truesync.category')),
            ],
            options={
                'db_table': 'courses',
            },
        ),
    ]