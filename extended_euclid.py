from euclid import Euclid


class Extended_Euclid:
    def __init__(self):
        pass


    def eea(self, verbosity, a, b):
        euc = Euclid()
        if(verbosity>=1):
            print("[INFO]:    Starting Extended Euclidean Algorithm; A = {}, B = {}".format(a,b))

        
        
        if a<b:
            r = [b, a]
        else:
            r =[a, b]
        
        i = 1
        s = [1, 0]
        t = [0, 1]
        q = [0]
        if(verbosity>=2):
            print("______________________________________________")
        while True:
            i = i+1
            r.append(r[i-2] % r[i-1])
            q.append( int((r[i-2]-r[i])/r[i-1]) )
            s.append(s[i-2]-q[i-1]*s[i-1])        
            t.append(t[i-2]-q[i-1]*t[i-1])
            #print("i: ",i,"qi-1: ",q[i-1],"r: ",r[i],"s: ",s[i],"t: ",t[i])

            if(verbosity>=2):
                print("| i: {} | qi-1: {} | r: {} | s: {} | t: {} |".format(i,q[i-1],r[i],s[i],t[i]))
            
            if r[i] == 0:
                break


        if euc.gcd(verbosity, a, b) != 1:
            if(verbosity>=1):
                print("[ERROR]:   Inverse does not exist.")
            return(0)
        else:
            if(verbosity>=1):
                print("[INFO]:    Extended EA done; Inverse of {} mod {} is: {}".format(r[0],r[1],t[i-1]))
            return t[i-1]