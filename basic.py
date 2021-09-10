#factorial
n=5
o=1
for i in range(1,n+1):
    o=o*i
    #print(o)
print(o)
--->120

#prime
l=7
for i in range(l):
    if(i%7==0):
        y=2
    else:
        y="no"
print(y)
--->no

#sum of end numbers
a="902345"
b="89756"
print(int(a[-1])+int(b[-1]))
--->11


#fibbonnic
p=8
m,n=-1,1
s=""
for i in range(1,p+1):
    k=m+n
    m=n
    n=k
    #print(k)
    s+=str(k)+","
print(s)
--->0,1,1,2,3,5,8,13
