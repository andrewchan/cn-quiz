from unittest2 import TestCase
from dict_mapping import dict_mapping

class DictMappingTest(TestCase):

    def test_result_is_not_none(self):
        self.assertIsNotNone(dict_mapping())

    def test_result_is_dict(self):
        self.assertIsInstance(dict_mapping(), dict)

    def test_key_val_type(self):
        for k, v in dict_mapping().iteritems():
            self.assertIsInstance(k, int)
            self.assertIn(type(v), [int, float])


    