# Generated by Django 4.1.7 on 2023-03-02 08:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0004_image_hight_image_name_image_width'),
    ]

    operations = [
        migrations.RenameField(
            model_name='image',
            old_name='hight',
            new_name='height',
        ),
    ]