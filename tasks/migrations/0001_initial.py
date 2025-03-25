# Generated by Django 5.1.7 on 2025-03-25 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('completed_at', models.DateTimeField(blank=True, null=True)),
                ('task_type', models.CharField(choices=[('DEV', 'Development'), ('DSN', 'Design'), ('TST', 'Testing'), ('MTG', 'Meeting'), ('OTH', 'Other')], default='OTH', max_length=3)),
                ('status', models.CharField(choices=[('NS', 'Not Started'), ('IP', 'In Progress'), ('CP', 'Completed'), ('OH', 'On Hold')], default='NS', max_length=2)),
            ],
        ),
    ]
