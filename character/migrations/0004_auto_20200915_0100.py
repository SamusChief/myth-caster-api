# Generated by Django 3.1.1 on 2020-09-15 01:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('character', '0003_auto_20200915_0039'),
    ]

    operations = [
        migrations.AlterField(
            model_name='character',
            name='class_levels',
            field=models.ManyToManyField(related_name='characters_with_class_and_level', to='character.ClassAndLevel'),
        ),
        migrations.AlterField(
            model_name='character',
            name='inventory_adventuring_gear',
            field=models.ManyToManyField(related_name='characters_with_gear', to='character.InventoryAdventuringGear'),
        ),
        migrations.AlterField(
            model_name='character',
            name='inventory_armors',
            field=models.ManyToManyField(related_name='characters_with_armor', to='character.InventoryArmor'),
        ),
        migrations.AlterField(
            model_name='character',
            name='inventory_tools',
            field=models.ManyToManyField(related_name='characters_with_tool', to='character.InventoryTool'),
        ),
        migrations.AlterField(
            model_name='character',
            name='inventory_weapons',
            field=models.ManyToManyField(related_name='characters_with_weapon', to='character.InventoryWeapon'),
        ),
        migrations.AlterField(
            model_name='character',
            name='inventory_wondrous_items',
            field=models.ManyToManyField(related_name='characters_with_wondrous_item', to='character.InventoryWondrousItem'),
        ),
        migrations.AlterField(
            model_name='character',
            name='skills',
            field=models.ManyToManyField(related_name='characters_with_skill_proficiency', to='character.SkillProficiency'),
        ),
        migrations.AlterField(
            model_name='characterclass',
            name='features',
            field=models.ManyToManyField(related_name='character_class_with_features', to='character.FeaturesAtLevel'),
        ),
        migrations.AlterField(
            model_name='characterclass',
            name='spell_slots',
            field=models.ManyToManyField(related_name='character_class_with_spell_slots', to='character.SpellSlotsAtLevel'),
        ),
        migrations.AlterField(
            model_name='characterclass',
            name='spells_known',
            field=models.ManyToManyField(related_name='character_class_with_spells_known', to='character.SpellsKnownAtLevel'),
        ),
    ]