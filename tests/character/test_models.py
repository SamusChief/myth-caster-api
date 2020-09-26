""" Unit Tests for the characters.models module """
from ddf import G

from rest_framework.test import APITestCase

from character.models import Character, CharacterClass, ClassAndLevel, SkillProficiency, \
    Ancestry, SubAncestry
from skills.models import Skill


class CharacterModelTestCase(APITestCase):
    """ Tests for the Character model property functions. """
    def test_proficiency_bonus(self):
        """ Test that proficiency bonus calculation is equal to CEIL(LEVEL / 4) + 1"""
        char_class_1 = G(CharacterClass)
        class_1_and_level = G(ClassAndLevel, character_class=char_class_1, level=5)
        char_class_2 = G(CharacterClass)
        class_2_and_level = G(ClassAndLevel, character_class=char_class_2, level=3)
        character = G(Character, class_levels=[class_1_and_level.id, class_2_and_level.id])

        self.assertEqual(character.proficiency_bonus, 3, \
            msg="Total level is 8, proficiency should be 3")

        char_class_3 = G(CharacterClass)
        class_3_and_level = G(ClassAndLevel, character_class=char_class_3, level=1)
        character.class_levels.add(class_3_and_level)

        self.assertEqual(character.proficiency_bonus, 4, \
            msg="Total level is now 9, proficiency should bump by 1")

    def test_initiative(self):
        """ Test that initiative modifier is calculated accounting for 
        dexterity, jack of all trades, and miscellaneous bonuses """
        char_class_1 = G(CharacterClass)
        class_1_and_level = G(ClassAndLevel, character_class=char_class_1, level=5)
        character = G(Character, class_levels=[class_1_and_level.id])
        self.assertEqual(character.initiative, 0)

        character.dexterity = 14
        self.assertEqual(character.initiative, 2)

        character.jack_of_all_trades = True
        self.assertEqual(character.initiative, 3)

        character.misc_initiative_bonus = 5
        self.assertEqual(character.initiative, 8)

    def test_ability_modifier_getters(self):
        """ Test that ability modifiers are calculated correctly """
        character = G(Character)
        self.assertEqual(character.strength_modifier, 0)

        character.strength += 4
        self.assertEqual(character.strength_modifier, 2)

        character.strength -= 8
        self.assertEqual(character.strength_modifier, -2)

    def test_all_proficiencies_list(self):
        """ Test that proficiencies list getter assembles properly from character attributes """
        p_skill = G(Skill, name='Proficient Skill')
        e_skill = G(Skill, name='Expert Skill')
        skill_proficiency = G(SkillProficiency, skill=p_skill, proficiency_level='P')
        skill_expertise = G(SkillProficiency, skill=e_skill, proficiency_level='E')
        character = G(Character, skills=[skill_proficiency.id, skill_expertise.id])
        character.proficient_heavy_armor = True
        character.proficient_languages= 'Common,Dwarvish'
        character.proficient_other = 'Other Proficiency A,Other Proficiency B'

        result = character.all_proficiencies_list

        self.assertIn('Proficient Skill', result)
        self.assertIn('Expert Skill', result)
        self.assertIn('Heavy Armor', result)
        self.assertIn('Common', result)
        self.assertIn('Dwarvish', result)
        self.assertIn('Other Proficiency A', result)
        self.assertIn('Other Proficiency B', result)

        self.assertNotIn('Light Armor', result)
        self.assertNotIn('Elvish', result)

    def test_all_proficiencies_dict(self):
        """ Test that proficiencies dict getter assembles properly from character attributes """
        p_skill = G(Skill, name='Proficient Skill')
        e_skill = G(Skill, name='Expert Skill')
        skill_proficiency = G(SkillProficiency, skill=p_skill, proficiency_level='P')
        skill_expertise = G(SkillProficiency, skill=e_skill, proficiency_level='E')
        character = G(Character, skills=[skill_proficiency.id, skill_expertise.id])
        character.proficient_heavy_armor = True
        character.proficient_languages= 'Common,Dwarvish'
        character.proficient_other = 'Other Proficiency A,Other Proficiency B'

        result = character.all_proficiencies_dict

        self.assertIn('armor', result)
        self.assertIn('weapons', result)
        self.assertIn('tools', result)
        self.assertIn('skills', result)
        self.assertIn('other', result)
        self.assertIn('languages', result)

        self.assertIn('Proficient Skill', result['skills'])
        self.assertIn('Expert Skill', result['skills'])
        self.assertIn('Heavy Armor', result['armor'])
        self.assertIn('Common', result['languages'])
        self.assertIn('Dwarvish', result['languages'])
        self.assertIn('Other Proficiency A', result['other'])
        self.assertIn('Other Proficiency B', result['other'])

        self.assertNotIn('Light Armor', result['armor'])
        self.assertNotIn('Elvish', result['languages'])


class AncestryModelTestCase(APITestCase):
    """ Test class for the ancestry model properties """
    def test_has_child(self):
        """ Test that the has_child property correctly determines when an
        ancestry has a child ancestry """
        ancestry_no_children = G(Ancestry)
        ancestry_has_children = G(Ancestry)
        G(SubAncestry, parent=ancestry_has_children)

        self.assertTrue(ancestry_has_children.has_child)
        self.assertFalse(ancestry_no_children.has_child)
