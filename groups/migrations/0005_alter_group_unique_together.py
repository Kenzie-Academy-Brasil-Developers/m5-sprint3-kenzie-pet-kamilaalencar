# Generated by Django 4.0.5 on 2022-06-27 01:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0004_alter_group_unique_together'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='group',
            unique_together=set(),
        ),
    ]
