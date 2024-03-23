def check(n):
    l= n%10
    if l==5:
        return n**2
    elif l==3:
        return n**3
    elif l==6:
        return n-1
    else:
        return n/2
a=check(13)
print(a)    