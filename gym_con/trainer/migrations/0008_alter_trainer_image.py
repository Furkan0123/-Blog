# Generated by Django 4.2.11 on 2024-04-21 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trainer', '0007_alter_trainer_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trainer',
            name='image',
            field=models.ImageField(default='trainer/default_indir.jpeg', upload_to='trainer/%Y/%m/%d/'),
        ),
    ]