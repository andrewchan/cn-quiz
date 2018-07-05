from unittest2 import TestCase
from circle import Circle

class CircleTests(TestCase):
    
    def test_new_instance_with_valid_input(self):
        c = Circle(10)
        c2 = Circle(3, 'red')
        self.assertEqual(c.radius, 10)
        self.assertEqual(c.color, None)
        self.assertEqual(c2.radius, 3)
        self.assertEqual(c2.color, 'red')

    def test_new_instance_with_invalid_input(self):
        inputs = [0, None, -1, '1']
        for input in inputs:
            with self.assertRaises(Exception) as context:
                Circle(input)
            self.assertIn("Invalid radius", context.exception)
        

    def test_valid_color(self):
        # tesitng #3
        c1 = Circle(1, 'red')
        c2 = Circle(1, 'green')
        c3 = Circle(1, 'blue')
        
        self.assertTrue(c1.has_valid_color())
        self.assertTrue(c2.has_valid_color())
        self.assertTrue(c3.has_valid_color())
        
    def test_invalid_color(self):
        c1 = Circle(5)
        c2 = Circle(2, 'brown')
        c3 = Circle(3, 'BLUE')

        self.assertFalse(c1.has_valid_color())
        self.assertFalse(c2.has_valid_color())
        self.assertFalse(c3.has_valid_color())
           
    def test_circle_by_radius(self):
        # testing #4
        c1 = Circle.new_instance_by_radius(10)
        c2 = Circle.new_instance_by_radius(10)
        self.assertEqual(type(c2), Circle)
        self.assertNotEqual(c1, c2)

    def test_circumference_to_radius(self):
        self.assertAlmostEqual(Circle.circumference_to_radius(62.83), 10.0047, 3)

    def test_circle_by_circumference_valid_input(self):
        # testing #5
        c1 = Circle.new_instance_by_circumference(62.83)
        self.assertAlmostEqual(c1.radius, 10.0047, 3)

    def test_circle_by_circumference_invalid_input(self):
        with self.assertRaises(Exception) as context:
            Circle.new_instance_by_circumference(None)
        self.assertIn("Invalid Circumference", context.exception)

    def test_get_circumference_by_radius_invalid_input(self):
        inputs = [0, None, -1, '2']
        for input in inputs:
            with self.assertRaises(Exception) as context:
                Circle.get_circumference_by_radius(input)
            self.assertIn("Invalid radius", context.exception)

    def test_get_circumference_by_radius_valid_input(self):
        # testing #6
        self.assertAlmostEqual(Circle.get_circumference_by_radius(10), 62.83, 1)
        

    def test_instance_method_get_circumference(self):
        # testing #7
        c1 = Circle(10)
        self.assertAlmostEqual(c1.get_circumference(), 62.83, 1)

    def test_get_area_by_radius_valid_input(self):
        self.assertEqual(Circle.get_area_by_radius(10), 314)

    def test_get_area_by_radius_invalid_input(self):
        inputs = [0, None, -1, '2']
        for input in inputs:
            with self.assertRaises(Exception) as context:
                Circle.get_area_by_radius(input)
            self.assertIn("Invalid radius", context.exception)

    def test_get_area(self):
        # testing #8
        c1 = Circle(10)
        self.assertAlmostEqual(c1.get_area(), 314)

    def test_get_area_by_scale_factor(self):
        # testing #9
        original_radius = 10
        c1 = Circle(original_radius)
        self.assertEqual(c1.get_area_of_scaled_circle(50), 3.14 * (original_radius/2)**2 )

    def test_get_area_by_scale_factor_with_zero(self):
        radius = 10
        c1 = Circle(radius)
        self.assertEqual(c1.get_area_of_scaled_circle(0), 3.14 * radius**2)


    def test_instance_method_area_scale_dict(self):
        # testing # 10
        radius = 10
        c1 = Circle(radius)
        scale_dict = c1.area_scale_dict()
        for k, v in scale_dict.iteritems():
            self.assertAlmostEqual(v, 3.14 * (radius * float(k)/100)**2, 1)