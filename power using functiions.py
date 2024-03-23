def power(n,m):
    if m==0:
        return 1   
    return n*power(n,m-1)
a=power(0,4)
print(a)