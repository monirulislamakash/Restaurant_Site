# Generated by Django 3.1.2 on 2021-02-08 10:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0017_auto_20210208_1647'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 2, 8, 16, 47, 50, 949569)),
        ),
    ]
