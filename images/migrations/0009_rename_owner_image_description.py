# Generated by Django 4.1.7 on 2023-03-05 20:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0008_alter_image_owner'),
    ]

    operations = [
        migrations.RenameField(
            model_name='image',
            old_name='owner',
            new_name='description',
        ),
    ]
