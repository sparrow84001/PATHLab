# Generated by Django 3.2.3 on 2021-07-01 15:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='emp',
            old_name='email',
            new_name='exampleInputEmail1',
        ),
        migrations.RenameField(
            model_name='emp',
            old_name='password',
            new_name='exampleInputPassword1',
        ),
    ]
