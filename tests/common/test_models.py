""" Unit Tests for the common.models module """
from rest_framework.test import APITestCase

from common.models import OwnedModel


class OwnedModelTestCase(APITestCase):
    """ Test Case for the OwnedModel abstract class """
    def test_new_owned_model_subclass_has_attributes(self):
        """ Test that new instances of OwnedModels gain the owner and
        authorized_editors attributes"""
        class OwnedModelChild(OwnedModel):
            """ Dummy class for testing """

        self.assertTrue(hasattr(OwnedModelChild, 'owner'))
        self.assertTrue(hasattr(OwnedModelChild, 'authorized_editors'))
