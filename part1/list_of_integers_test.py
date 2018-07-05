from unittest2 import TestCase
from list_of_integers import list_of_integers

class ListOfIntegersTests(TestCase):

    def test_is_not_none(self):
        self.assertIsNotNone(list_of_integers())
        
    def test_return_is_list(self):
        self.assertIsInstance(list_of_integers(), list)

    def test_element_is_int(self):
        for i in list_of_integers():
            self.assertEqual(type(i), int)



