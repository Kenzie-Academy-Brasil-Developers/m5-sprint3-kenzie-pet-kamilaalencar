# Generated by Django 4.0.5 on 2022-06-27 01:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0003_alter_group_name_alter_group_scientific_name'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='group',
            unique_together={('name', 'scientific_name')},
        ),
    ]