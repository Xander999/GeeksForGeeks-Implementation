'''
https://practice.geeksforgeeks.org/problems/consecutive-1s-not-allowed/0
'''


def count(n):
    a=[0 for x in range(n)]
    b=[0 for x in range(n)]
    a[0]=b[0]=1
    for i in range(1,n):
        a[i] = a[i-1] + b[i-1] 
        b[i] = a[i-1]
    return ((a[n-1]+b[n-1])%1000000007)
    
def fibo(n):
    c=0
    a=0
    b=1
    for i in range(n-1):
        c=a+b
        a=b
        b=c
    return c

a=int(input())

while(a>0):
    
    x=int(input())
    p=count(x)
    print(p)
    a=a-1
