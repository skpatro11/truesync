# Generated by Django 4.0.4 on 2022-05-25 12:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('truesync', '0003_added_course_model'),
    ]

    operations = [
        migrations.CreateModel(
            name='Enrollment',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(db_index=True, default=True)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='course_enrollments', to='truesync.course')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_enrollments', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'enrollments',
            },
        ),
    ]
