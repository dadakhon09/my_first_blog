# Generated by Django 2.2.2 on 2019-06-19 12:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20190619_1208'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='comment',
            new_name='content',
        ),
    ]