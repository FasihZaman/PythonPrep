import math
a=int(input())
for _ in range(a):
    b=int(input())
    c=int(input())
    n=b+c-1
    r=b-1
    f=math.factorial
    k=f(n)//f(r)//f(n-r)
    if((len(str(k)))>9):
        print(int(str(k)[-9:]))
    else:
        print(k)
