# Generated by Django 3.1.1 on 2020-09-21 23:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spells', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='spell',
            name='school',
            field=models.CharField(choices=[('A', 'Abjuration'), ('C', 'Conjuration'), ('D', 'Divination'), ('EN', 'Enchantment'), ('EV', 'Evocation'), ('I', 'Illusion'), ('N', 'Necromancy'), ('T', 'Transmutation')], db_index=True, default='A', max_length=2),
            preserve_default=False,
        ),
    ]
