# Generated by Django 3.1.4 on 2021-01-02 01:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField(blank=True)),
                ('status', models.PositiveIntegerField(choices=[(0, 'backlog'), (1, 'todo'), (2, 'in progress'), (3, 'done')], default=0)),
            ],
        ),
    ]
