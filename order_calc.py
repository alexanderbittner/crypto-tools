class Order_Calc:
    def __init__(self):
        pass

    def order(self, verbosity, a, b):
        order = a
        group = b
        if(verbosity>=1):
            print("[INFO]:    trying to compute order of {} in group {}".format(order, group))
        exp = 1
        while((order**exp)%group!=1):
            if(verbosity>=2):
                print("[INFO]:    {} ^ {} mod {} = {}".format(order,exp,group,(order**exp)%group))
            exp = exp+1
        if(verbosity>=2):
            print("[INFO]:    {} ^ {} mod {} = {}".format(order,exp,group,(order**exp)%group))
        elif(verbosity==1):
            print("[INFO]:    Order of {} in Group {} is {}".format(a,b,exp))
        return exp