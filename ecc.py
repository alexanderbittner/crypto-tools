from extended_euclid import eea
class Curve:
    
    def __init__(self, a, b, p):
        self.param_a = a
        self.param_b = b
        self.param_p = p

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

testpoint1 = Point(35, 17)
testpoint2 = Point(3, 36)
testcurve = Curve(2, 5, 37)

def check(point, curve): #checks if the point is on the curve
    y = (point.y * point.y) % curve.param_p
    x = (point.x * point.x * point.x + curve.param_a * point.x + curve.param_b) % curve.param_p
    if y == x:
        return 1
    else:
        return 0

def point_add(point1, point2, curve):
    if check(point1, curve) == 0 or check(point2, curve) == 0:
        print("point is not on curve.")
        return(0)
    inv = eea(((point2.x - point1.x)%curve.param_p), curve.param_p)
    s = ((point2.y - point1.y)*inv) % curve.param_p
    new_x = (s*s - point1.x - point2.x) % curve.param_p
    new_y = (s*(point1.x - new_x)-point1.y) % curve.param_p
    point3 = Point(new_x, new_y)
    print ("New Point: (",new_x,",",new_y,")")
    return(point3)

newPoint = point_add(testpoint1, testpoint2, testcurve) #test