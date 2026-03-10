import math

tree=[[3,5],[6,9],[1,2],[0,-1]]

def alphabeta(d,i,maxi,a,b):
    if d==2: return tree[i][0]
    if maxi:
        v=-math.inf
        for j in range(2):
            v=max(v,alphabeta(d+1,i*2+j,False,a,b))
            a=max(a,v)
            if b<=a: break
        return v
    else:
        v=math.inf
        for j in range(2):
            v=min(v,alphabeta(d+1,i*2+j,True,a,b))
            b=min(b,v)
            if b<=a: break
        return v

print("Optimal value:",alphabeta(0,0,True,-math.inf,math.inf))
