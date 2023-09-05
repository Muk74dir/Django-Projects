# Generated by Django 4.2.4 on 2023-09-05 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_alter_articlemodel_category_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articlemodel',
            name='category',
            field=models.CharField(choices=[('Latest', 'Latest'), ('Sports', 'Sports'), ('Business', 'Business'), ('Entertainment', 'Entertainment'), ('Technology', 'Technology'), ('Science', 'Science'), ('Health', 'Health')], max_length=20),
        ),
        migrations.AlterField(
            model_name='articlemodel',
            name='rating',
            field=models.CharField(choices=[('4', '4'), ('1', '1'), ('2', '2'), ('0', '0'), ('3', '3')], max_length=10),
        ),
        migrations.AlterField(
            model_name='categorymodel',
            name='category_name',
            field=models.CharField(choices=[('Latest', 'Latest'), ('Sports', 'Sports'), ('Business', 'Business'), ('Entertainment', 'Entertainment'), ('Technology', 'Technology'), ('Science', 'Science'), ('Health', 'Health')], max_length=20),
        ),
    ]
