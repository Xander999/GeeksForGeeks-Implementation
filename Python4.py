'''
https://practice.geeksforgeeks.org/problems/maximum-index/0
'''
n=int(input())
while(n>0):
    rt=int(input())-1
    l=0
    s=[]
    s=input().split()
    st=[int(x) for x in s]
    ma=0
    for i in range(rt):
        l=i
        r=rt
        m=0
        while(l<=r):
            if(st[l]<=st[r]):
                m=r-l
                if(ma<m):
                    ma=m
                break
            r=r-1
    print(ma)
    n=n-1
