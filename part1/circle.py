

class Circle(object):
    """
    Following Python best practices, define a class structure for a Circle
    with static methods, class methods, instance methods, and properties
    via instance methods. The class must:
    1. inherit from object,
    2. include a base initializer that stores a radius and optional color,
    3. provide a method to validate if a color is "red", "green", or "blue",
    returning True when a color is valid, and False in all other cases
    4. provide a method for creating a circle instance from a radius,
    5. provide a method for creating a circle instance rom a circumference, 
    6. provide a method for calculating a circumference from a radius, 
    7. provide a method to return circumference of the circle,
    8. provide a method to return area of the circle,
    9. provide a method to return the area of a circle scaled by provided factor
    (area of a circle which radius has been scaled by provided factor).
    10. implement the following Circle method:
    def area_scale_dict(self):
    '''
    Return a dictionary of circle radiuses mapped to area of the Circle from 10% 
    of the radius up to 100% (the radius), incrementing by 5% with each step.
    '''

    """
    
    def __init__(self, radius, color=None):
        if not radius or type(radius) not in [int, float, long]:
            raise Exception("Invalid radius")
        elif radius <= 0:
            raise Exception("Invalid radius")
        else:
            self._radius = radius
        self._color = color

    @property
    def radius(self):
        return self._radius

    @property
    def color(self):
        return self._color

    def has_valid_color(self):
        if self.color in ['red', 'green', 'blue']:
            return True
        else:
            return False

    @classmethod
    def new_instance_by_radius(cls, radius):
        return cls(radius)

    @classmethod
    def new_instance_by_circumference(cls, circ):
        return cls(Circle.circumference_to_radius(circ))

    @staticmethod
    def circumference_to_radius(circ):
        if not circ or type(circ) not in [int, long, float]:
            raise Exception("Invalid Circumference")
        elif circ <= 0:
            raise Exception("Invalid Circumference")
        else:
            return circ/(2*3.14)

    @staticmethod
    def get_circumference_by_radius(radius):
        if not radius or type(radius) not in [int, long, float]:
            raise Exception("Invalid radius")
        elif radius <= 0:
            raise Exception("Invalid radius")
        else:
            return 2 * 3.14 * radius

    @staticmethod
    def get_area_by_radius(radius):
        if not radius or type(radius) not in [int, long, float]:
            raise Exception("Invalid radius")
        elif radius <= 0:
            raise Exception("Invalid radius")
        else:
            return 3.14 * radius ** 2

    def get_circumference(self):
        return self.get_circumference_by_radius(self.radius)

    def get_area(self):
        return Circle.get_area_by_radius(self.radius)
    
    def get_area_of_scaled_circle(self, factor):
        
        if factor is None or type(factor) not in [int, long, float]:
            raise Exception("Invalid factor")
        elif factor < 0:
            raise Exception("Invalid factor")
        elif factor == 0:
            return self.get_area()
        else:
            return Circle.get_area_by_radius(self.radius * float(factor) / 100)
    
    def area_scale_dict(self):
        '''
        Return a dictionary of circle radiuses mapped to area of the Circle from 10% 
        of the radius up to 100% (the radius), incrementing by 5% with each step.
        '''
        scale_dict = {}
        for i in xrange(5, 101, 5):
            scale_dict[i] = Circle.get_area_by_radius(self.radius * float(i)/100)

        return scale_dict