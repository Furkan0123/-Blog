# Generated by Django 4.2.11 on 2024-04-22 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trainer', '0013_rename_category_trainer_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, null=True)),
                ('slug', models.SlugField(null=True, unique=True)),
            ],
        ),
    ]
