# Generated by Django 3.1.1 on 2020-09-21 23:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('spells', '0002_spell_school'),
    ]

    operations = [
        migrations.RenameField(
            model_name='spell',
            old_name='classes',
            new_name='character_classes',
        ),
    ]
