# Generated by Django 5.1 on 2024-10-20 16:53

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cyberpolygonApp', '0015_rename_answers_answer_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='correctanswer',
            name='answer_id',
        ),
        migrations.RemoveField(
            model_name='correctanswer',
            name='question_id',
        ),
        migrations.RemoveField(
            model_name='question',
            name='test_id',
        ),
        migrations.RemoveField(
            model_name='task',
            name='flag',
        ),
        migrations.RemoveField(
            model_name='task',
            name='is_active',
        ),
        migrations.AlterField(
            model_name='task',
            name='title',
            field=models.TextField(max_length=100, unique=True),
        ),
        migrations.CreateModel(
            name='UserDoingTask',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('flag', models.TextField(max_length=100)),
                ('vagrant_password', models.TextField(max_length=50)),
                ('is_active', models.BooleanField()),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cyberpolygonApp.task')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='Answer',
        ),
        migrations.DeleteModel(
            name='CorrectAnswer',
        ),
        migrations.DeleteModel(
            name='Question',
        ),
        migrations.DeleteModel(
            name='Test',
        ),
    ]
