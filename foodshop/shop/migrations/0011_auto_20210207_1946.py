# Generated by Django 3.1.2 on 2021-02-07 13:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0010_auto_20210207_1942'),
    ]

    operations = [
        migrations.RenameField(
            model_name='slidehead',
            old_name='text1',
            new_name='nameone',
        ),
        migrations.RenameField(
            model_name='slidehead',
            old_name='text2',
            new_name='nametow',
        ),
        migrations.RenameField(
            model_name='sliderimages',
            old_name='image1',
            new_name='pic1',
        ),
        migrations.RenameField(
            model_name='sliderimages',
            old_name='image2',
            new_name='pic2',
        ),
    ]
