'''
1. take the time.
2. take the no of cookies eaten.
3. take the number of glass milk drank.
4. set a counter to check milk and cookies and foloowed instruction.
5. if cookie ate and milk drank.
6. increase the onstructioin counter by 1.
7. if instruction followed yes.
8. if not followed no.
'''

T=int(input()) #take the input as minutes
for i in range(T): #in every minute
    N=int(input()) #he eats cookie
    s=list(map(str,input().split())) #he drinks milk
    s1=s.count('cookie') #count cookie
    s2=s.count('milk') #count milk
    s3=0 #counter to follow instruction
    for i in range(N-1): #till whole time bear is in kitchen
        if(s[i]=='cookie' and s[i+1]=='milk'): #if he eats cookie and drink milk 
            s3+=1 #increase s3 to 1
            
            
    if(s3==s1): #instrction followed 
        print('YES') #yes
    elif(s1==0 and s2>0): #if eaten more cookies and drink milk after
        print('YES') #still instruction followed
    else:
        print('NO') #else not followed
