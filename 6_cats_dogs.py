'''
1. take no of cats, dogs and legs.
2. count the total no of legs.
3. counted legs does not exceed the total leg
4. if total legs and counted legs match
5. counting is correct
6. check for the missing cats leg, dog can hold 2 cats max so 4*2 legs can be missing.
7. counting is correct.
8. wrong counting.
'''

t=int(input()) #take input as no of cat and dogs and legs counted
for i in range(t): #in the list
    c,d,l=map(int,input().split()) #split the count separately as cats, dogs and legs
    tot=c*4+d*4 #summing the total legs of cats and dogs
    if(l%4==0 and l<=tot): #assuming every pet has 4 legs and counted legs does not exceed the total leg
        if(c<=2*d and l>=d*4): #if total legs and counted legs match
            print("yes") #counting is correct
        elif(c>2*d and l>=(c-2*d+d)*4): #for if some cat is missing then 4 legs will be less
            print("yes") #counting is correct
        else: #wrong counting
            print("no")
    else:
        print("no")
