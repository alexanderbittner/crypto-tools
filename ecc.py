from extended_euclid import Extended_Euclid

class Curve:
        # Curve constructor
        def __init__(self, a, b, p):
            self.param_a = a
            self.param_b = b
            self.param_p = p

class Point:
    # Point constructor
    def __init__(self, x, y):
        self.x = x
        self.y = y

        self.is_neutral = False

        # this point is a neutral element!
        if self.x == float('inf') and self.y == float('inf'):
            self.is_neutral = True


class Elliptic_Curves:
    def __init__(self):
        pass        

    # checks if a proved point is on a provided curve
    def check(self, verbosity, point, curve):
        if verbosity>=1:
            print("[INFO]:    Checking if point ({}, {}) is on curve".format(point.x, point.y))

        # can't be on the curve if point is neutral element
        if point.is_neutral == True:
            return 1

        # check if point is actually on the curve, return result
        y = (point.y * point.y) % curve.param_p
        x = (point.x * point.x * point.x + curve.param_a * point.x + curve.param_b) % curve.param_p
        if y == x:
            return 1
        else:
            return 0
    
    # doubles a point on a provided curve and returns the new point as a point object
    def point_double(self, verbosity, point, curve):
        Ex = Extended_Euclid()

        # make sure the point is on the curve before proceeding
        if self.check(verbosity, point, curve) == 0:
            if(verbosity>=0):
                print("[ERROR]:   Point is not on curve.")
            return 0

        # first check for neutrality, then double the point & return the new point
        if point.is_neutral == True:
            new_x = float('inf')
            new_y = float('inf')
        else:
            inv = Ex.eea(verbosity, ((2*point.y)%curve.param_p), curve.param_p)    
            s = ((3*(point.x*point.x))+curve.param_a)*inv
            new_x = (s*s - point.x - point.x) % curve.param_p
            new_y = (s*(point.x - new_x)-point.y) % curve.param_p
    
        point3 = Point(new_x, new_y)
        return point3

    # adds two points together on a provided curve and returns the new point as a point object
    def point_add(self, verbosity, point1, point2, curve):
        Ex = Extended_Euclid()
        k = 1

        # make sure the points are on the curve before proceeding
        if self.check(verbosity, point1, curve) == 0:
            if(verbosity>=0):
                print("[ERROR]:   Point 1 is not on curve.")
            return(0)
        if self.check(verbosity, point2, curve) == 0:
            if(verbosity>=0):
                print("[ERROR]:   Point 2 is not on curve.")
            return(0)

        if(verbosity>=1):
            print("[INFO]:    Computing ({}, {}) + ({}, {})".format(point1.x, point1.y, point2.x, point2.y))
        
        # first check for neutrality
        if point1.is_neutral == True:
            new_x = point2.x
            new_y = point2.y
            k = 0
        if point2.is_neutral == True:
            new_x = point1.x
            new_y = point1.y
            k = 0
        
        # result is the neutral element
        if point1.x == point2.x and point1.y == (-point2.y)%curve.param_p:
            new_x = float('inf')
            new_y = float('inf')
            k = 0 

        # points are the same, so use point_double instead
        if point1.x == point2.x and point1.y == point2.y:
            return self.point_double(verbosity, point1, curve)

        # add the points & return the new point
        if k != 0:
            inv = Ex.eea(verbosity, ((point2.x - point1.x)%curve.param_p), curve.param_p)
            s = ((point2.y - point1.y)*inv) % curve.param_p
            new_x = (s*s - point1.x - point2.x) % curve.param_p
            new_y = (s*(point1.x - new_x)-point1.y) % curve.param_p
        
        point3 = Point(new_x, new_y)
        return(point3)

    # substracts two points from each other on a provided curve and returns the new point as a point object
    def point_substract(self, verbosity, point1, point2, curve):
        
        # are the points on the curve?
        if self.check(verbosity, point1, curve) == 0: 
            print("[ERROR]:   Point 1 is not on curve.")
            return(0)
        if self.check(verbosity, point2, curve) == 0:
            print("[ERROR]:   Point 2 is not on curve.")
            return(0)            
        
        if(verbosity>=1):
            print("[INFO]:    Computing ({}, {}) - ({}, {})".format(point1.x, point1.y, point2.x, point2.y))
        
        # check for neutrality, then modify second point & pass on to point_add
        if point2.is_neutral == True:
            neg_point2 = point2
        else:
            neg_point2 = Point(point2.x, (-point2.y % curve.param_p))
        
        return self.point_add(verbosity, point1, neg_point2, curve)