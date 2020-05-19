from extended_euclid import Extended_Euclid



class Curve:
        def __init__(self, a, b, p):
            self.param_a = a
            self.param_b = b
            self.param_p = p

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.is_neutral = False
        if self.x == float('inf') and self.y == float('inf'):
            self.is_neutral = True


class Elliptic_Curves:
    def __init__(self):
        pass        

    def check(self, verbosity, point, curve): #checks if the point is on the curve
        if verbosity>=1:
            print("[INFO]:    Checking if point ({}, {}) is on curve".format(point.x, point.y))
        if point.is_neutral == True:
            return 1
        y = (point.y * point.y) % curve.param_p
        x = (point.x * point.x * point.x + curve.param_a * point.x + curve.param_b) % curve.param_p
        if y == x:
            return 1
        else:
            return 0
    
    def point_double(self, verbosity, point, curve):
        Ex = Extended_Euclid()

        if self.check(verbosity, point, curve) == 0:
            print("[ERROR]:   Point is not on curve.")
            return 0
        if point.is_neutral == True:
            new_x = float('inf')
            new_y = float('inf')
        else:
            inv = Ex.eea(verbosity, ((2*point.y)%curve.param_p), curve.param_p)    
            s = ((3*(point.x*point.x))+curve.param_a)*inv
            new_x = (s*s - point.x - point.x) % curve.param_p
            new_y = (s*(point.x - new_x)-point.y) % curve.param_p
    
        point3 = Point(new_x, new_y)

        if point3.is_neutral == True:
            print("[INFO]:    Calculation done; New Point: O (neutral element)")
        else :
            print ("[INFO]:    Calculation done; New Point: (({}, {}))".format(point3.x, point3.y))
        return point3


    def point_add(self, verbosity, point1, point2, curve):
        Ex = Extended_Euclid()
        k = 1

        if self.check(verbosity, point1, curve) == 0: 
            print("[ERROR]:   Point 1 is not on curve.")
            return(0)
        if self.check(verbosity, point2, curve) == 0:
            print("[ERROR]:   Point 2 is not on curve.")
            return(0)            
        if(verbosity>=1):
            print("[INFO]:    Computing ({}, {}) + ({}, {})".format(point1.x, point1.y, point2.x, point2.y))
        
        if point1.is_neutral == True:
            new_x = point2.x
            new_y = point2.y
            k = 0
        if point2.is_neutral == True:
            new_x = point1.x
            new_y = point1.y
            k = 0
        
        if point1.x == point2.x and point1.y == (-point2.y)%curve.param_p:
            new_x = float('inf')
            new_y = float('inf')
            k = 0 
    
        if point1.x == point2.x and point1.y == point2.y:
            return self.point_double(verbosity, point1, curve)
 
        if k != 0:
            inv = Ex.eea(verbosity, ((point2.x - point1.x)%curve.param_p), curve.param_p)
            s = ((point2.y - point1.y)*inv) % curve.param_p
            new_x = (s*s - point1.x - point2.x) % curve.param_p
            new_y = (s*(point1.x - new_x)-point1.y) % curve.param_p
        
        point3 = Point(new_x, new_y)
        
        if point3.is_neutral == True:
            print ("[INFO]:    Calculation done; New Point: O (neutral element)")
        else:
            print ("[INFO]:    Calculation done; New Point: ({}, {})".format(point3.x, point3.y))
        
        return(point3)

    def point_substract(self, verbosity, point1, point2, curve):
        
        if self.check(verbosity, point1, curve) == 0: 
            print("[ERROR]:   Point 1 is not on curve.")
            return(0)
        if self.check(verbosity, point2, curve) == 0:
            print("[ERROR]:   Point 2 is not on curve.")
            return(0)            
        
        if(verbosity>=1):
            print("[INFO]:    Computing ({}, {}) - ({}, {})".format(point1.x, point1.y, point2.x, point2.y))
        if point2.is_neutral == True:
            neg_point2 = point2
        else:
            neg_point2 = Point(point2.x, (-point2.y % curve.param_p))
        
        return self.point_add(verbosity, point1, neg_point2, curve)

pointA = Point(3, 36)
PointB = Point(35, 17)
PointC = Point(float('inf'), float('inf'))
PointD = Point(148, 508)
testcurve = Curve(41, 299, 1051)
EC = Elliptic_Curves()
EC.point_double(1, PointD, testcurve)