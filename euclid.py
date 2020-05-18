class Euclid:
    def __init__(self):
        pass

    def gcd(self, verbosity, a, b):
        if(verbosity>=1):
            print("[INFO]:    Starting Euclidean Algorithm; A = {}, B = {}".format(a,b))

        while 1:
            remainder = a % b
            if(verbosity>=2):
                print("[INFO]:    R = A%B = {} % {} = {}".format(a,b,remainder))
            if not remainder:
                break
            a=b
            b=remainder
        if(verbosity>=1):
            print('[INFO]:    Euclidean Algorithm done; GCD is: {}'.format(b))
        return b