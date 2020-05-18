from euclid import gcd

def eea(a, b):
    print(a, b)
    if gcd(a, b) != 1:
        print("ERROR: Inverse does not exist.")
        return(0)
    print(a, b)
    if a<b:
        r = [b, a]
    else:
        r =[a, b]
    
    i = 1
    s = [1, 0]
    t = [0, 1]
    q = [0]
    while True:
        i = i+1
        r.append(r[i-2] % r[i-1])
        q.append((r[i-2]-r[i])/r[i-1])
        s.append(s[i-2]-q[i-1]*s[i-1])        
        t.append(t[i-2]-q[i-1]*t[i-1])
        print("i: ",i,"qi-1: ",q[i-1],"r: ",r[i],"s: ",s[i],"t: ",t[i])
        if r[i] == 0:
            break
    print("Inverse of",r[0],"mod",r[1],": ",t[i-1])
    return t[i-1]
eea(5, 37)
eea(2, 14)