# Generated by Django 4.2.11 on 2024-04-21 19:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trainer', '0012_rename_category_trainer_category'),
    ]

    operations = [
        migrations.RenameField(
            model_name='trainer',
            old_name='Category',
            new_name='category',
        ),
    ]