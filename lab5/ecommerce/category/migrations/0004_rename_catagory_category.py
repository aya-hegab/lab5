# Generated by Django 5.0.1 on 2024-02-05 08:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0003_alter_catagory_img'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Catagory',
            new_name='Category',
        ),
    ]