# Generated by Django 4.2.4 on 2023-08-24 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TODO_App', '0002_alter_taskmodel_is_completed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taskmodel',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='taskmodel',
            name='is_completed',
            field=models.BooleanField(default=False),
        ),
    ]
