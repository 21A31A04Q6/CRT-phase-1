s1=0
s2=0
for i in range(0,31):
    if i%6==0:
        s1=s1+i
    else:
        s2=s2+i
print(s1-s2)            