'''
https://practice.geeksforgeeks.org/problems/save-ironman/0
'''


def h(p):

    if((p>=48 and p<=57) or (p>=97 and p<=122)):
        return 1
    else:
        return 0


n=int(input())
while(n>0):
    st=str(input())
    st=st.lower()
    l=len(st)
    i=0
    j=l-1
    p=0
    while(i<j):
        a=ord(st[i])
        b=ord(st[j])

        if(h(a)==1 and h(b)==1):
            i=i+1
            j=j-1
            if(a!=b):
                p=1
            continue
            
        if(h(a)==0):
            i=i+1

        if(h(b)==0):
            j=j-1

    if(p==0):
        print('YES')
    else:
        print('NO')
    n=n-1
