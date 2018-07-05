from unittest2 import TestCase
from hypothesis import given, strategies as st
from generate_cubes_until import generate_cubes_until

class GenerateCubesUntilTests(TestCase):

    def test_invalid_input(self):
        self.assertListEqual(generate_cubes_until(None), [])
        self.assertListEqual(generate_cubes_until(''), [])
        self.assertListEqual(generate_cubes_until([1]), [])
        self.assertListEqual(generate_cubes_until(float('nan')), [])

    def test_zero_as_input(self):
        self.assertListEqual(generate_cubes_until(0), [])

    def test_one_as_input(self):
        self.assertListEqual(generate_cubes_until(1), [])

    @given(st.integers(1, 100000))
    def test_valid_positive_int_number(self, i):
        r = generate_cubes_until(i)
        self.assertTrue((len(r)+1)**3 % i == 0)

    def test_valid_negative_int_number(self):
        self.assertListEqual(generate_cubes_until(-25), [1, 8, 27, 64])
    
    # 16GB memory is not enough to run the following test. 
    #
    #@given(st.floats(1, 2))
    #def test_valid_positive_float_number(self, i):
    #    r = generate_cubes_until(i)
    #    self.assertTrue((len(r)+1)**3 % i == 0)
