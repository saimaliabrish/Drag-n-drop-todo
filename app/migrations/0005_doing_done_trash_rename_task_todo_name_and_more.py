# Generated by Django 4.1.7 on 2023-03-24 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Doing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Done',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Trash',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.RenameField(
            model_name='todo',
            old_name='task',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='todo',
            name='done',
        ),
        migrations.RemoveField(
            model_name='todo',
            name='pending',
        ),
        migrations.RemoveField(
            model_name='todo',
            name='todo',
        ),
        migrations.RemoveField(
            model_name='todo',
            name='trash',
        ),
    ]
