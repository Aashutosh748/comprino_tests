'''
1. choose sticks.
2. take the area.
3. count no of sticks so that none are broken.
4. matche the max area.
5. for a rectangle at least 4 sticks is reqd.
6. yes if area present.
'''

t=int(input()) #total no of sticks
for i in range(t): #choosing sticks
    c,d,l=map(int,input().split()) #forming the stuck, area and length
    tot=c*4+d*4 #total area 
    if(l%4==0 and l<=tot): #if sticks ok
        if(c<=2*d and l>=d*4): #if area matches
            print("yes") #yes
        elif(c>2*d and l>=(c-2*d+d)*4): #for a rectangle area at least 4 sticks are reqd
            print("yes")
        else:
            print("no")
    else:
        print("no")
