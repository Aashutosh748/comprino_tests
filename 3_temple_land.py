'''
1. choose the centre of the temple.
2. start the strip fronm 1.
3. increase the strip by 1 till centre. loop.
4. check the strip increasing, if else.
5. length should not exceed the temple centre.
6. check if the contidions are satisfied yes.
7. not satisfied no.
'''

n = int(input()) # take the length of the temple
for tc in range(n): #checking the temple
    a = int(input()) #input the centre
    l = list(map(int , input().split())) # list to hold the cordinates
    r = [0 for i in range(a)] #forming the centre of temple
    r[0]=1
    r[-1]=1 
    if len(l)%2==0: #if the first step doesnt start with 1 then invalid
        print('no')
    else:
        for i in range(1,len(l)//2+1): #checking the length and dimensions increasing of strip
            r[i]=r[i-1]+1 #increasing 1 at each step
            r[len(l)-i-1]=r[i] #moving to the next strip
        if r == l: 
            print('yes')
        else:
            print('no')
