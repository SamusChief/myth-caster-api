""" Unit Tests for the equipment.models module """
from ddf import G

from rest_framework.test import APITestCase

from equipment.models import Armor, Weapon, WeaponProperty


class MagicItemModelTestCase(APITestCase):
    """ Tests for the MagicItemModel mixin class """
    def test_is_magic(self):
        """ Test that the is_magic property properly determines if an item is magic """
        mundane_armor = G(Armor, rarity='M')
        magic_armor = G(Armor, rarity='C')

        self.assertTrue(magic_armor.is_magic)
        self.assertFalse(mundane_armor.is_magic)

class WeaponModelTestCase(APITestCase):
    """ Tests for the Weapon model """
    def setUp(self):
        self.ranged_longbow = G(WeaponProperty, name='ranged (150/600)')
        self.ranged_thrown = G(WeaponProperty, name='ranged (20/60)')
        self.finesse = G(WeaponProperty, name='finesse')
        self.thrown = G(WeaponProperty, name='thrown')
        self.versatile = G(WeaponProperty, name='versatile (d10)')

        self.handaxe = G(Weapon, properties=[self.thrown.id, self.ranged_thrown.id])
        self.dagger = G(Weapon, properties=[self.finesse.id, self.thrown.id, self.ranged_thrown.id])
        self.longbow = G(Weapon, properties=[self.ranged_longbow.id])
        self.rapier = G(Weapon, properties=[self.finesse.id])
        self.longsword = G(Weapon, properties=[self.versatile.id])

    def test_can_use_dex(self):
        """ Test that a weapon can use dexterity for attack/damage
        based on it having one of the dexterity properties """
        self.assertFalse(self.handaxe.can_use_dex, msg="Thrown non-finesse weapons use strength")
        self.assertTrue(self.dagger.can_use_dex, msg="Thrown finesse weapons can use dex")
        self.assertTrue(self.longbow.can_use_dex, msg="Ranged only weapons use dexterity")
        self.assertTrue(self.rapier.can_use_dex, msg="Finesse weapons can use either")
        self.assertFalse(self.longsword.can_use_dex, "Non finesse melee uses strength")

    def test_must_use_dex(self):
        """ Test that a weapon must use dexterity for attack/damage
        based on it having  """
        self.assertFalse(self.handaxe.must_use_dex, msg="Thrown non-finesse weapons use strength")
        self.assertFalse(self.dagger.must_use_dex, msg="Finesse weapons can use strength")
        self.assertTrue(self.longbow.must_use_dex, msg="Ranged only weapons use dexterity")
        self.assertFalse(self.rapier.must_use_dex, msg="Finesse weapons can use strength")
        self.assertFalse(self.longsword.must_use_dex, "Non finesse melee uses strength")
