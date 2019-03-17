'''
https://practice.geeksforgeeks.org/problems/reverse-words-in-a-given-string/0
'''
while(n>0):
    s=[]
    s=input().split('.')
    h=len(s)
    for x in range(h-1,-1,-1):
        if(x==0):
            print(s[x])
        else:
            print(s[x],end=".")
    n=n-1
