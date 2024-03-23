n=153
m=n
temp=n
sum=0
c=0
while n>0:  
    n=n//10
    c=c+1
while m>0:      
    a=m%10
    sum=sum+a**c
    m=m//10
if sum==temp:
    print("yes")
else:
    print("no")            