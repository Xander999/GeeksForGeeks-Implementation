'''
https://practice.geeksforgeeks.org/problems/is-binary-number-multiple-of-3/0
'''
while(n>0):
    s=input()
    k=0
    g=len(s)
    odd=0
    even=0
    for i in range(g-1,-1,-1):
        j=g-1-i
        if(s[i]=='1'):
            if(j%2==0):
                odd=odd+1
            else:
                even=even+1
                
    if((odd-even)%3==0):
        print('1')
    else:
        print('0')
        
    n=n-1
