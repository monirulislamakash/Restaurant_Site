# Generated by Django 3.1.2 on 2021-02-04 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(default='', max_length=50)),
                ('Email', models.CharField(default='', max_length=50)),
                ('Phone', models.CharField(default='', max_length=50)),
                ('Message', models.TextField(default='')),
            ],
        ),
    ]
