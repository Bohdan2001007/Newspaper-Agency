# Generated by Django 4.1.7 on 2023-03-10 12:29

from django.db import migrations
from django.core.management import call_command


def load_fixtures(state, schema_editor):
    call_command("loaddata", "Newspaper_Agency_db_data.json")


def reverse_load_fixtures(state, schema_editor):
    pass


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_alter_newspaper_options_alter_newspaper_redactors'),
    ]

    operations = [
        migrations.RunPython(load_fixtures, reverse_load_fixtures)
    ]