# Generated by Django 2.0.5 on 2019-08-04 00:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mtapp', '0004_box_office'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='box_office',
            name='collection',
        ),
        migrations.RemoveField(
            model_name='box_office',
            name='rank',
        ),
    ]