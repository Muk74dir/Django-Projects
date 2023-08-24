# Generated by Django 4.2.4 on 2023-08-24 04:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TaskModel',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('taskTitle', models.CharField(max_length=30)),
                ('taskDescription', models.CharField(max_length=50)),
                ('is_completed', models.BooleanField(default=False)),
            ],
        ),
    ]
