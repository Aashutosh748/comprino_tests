'''
1. input the members in the team and take the score.
2. if x has a higher score than other two then 
3. create a set arranged in order of the score.
4. create a function to compare the scores.
5. decide the order is valid or not using if else ladder.
6. if anyone has higher skill score then yes.
7. if such order is not possible then no.

'''

def result(a,b): #creating a function to compare result
    f1=(a[0] >= b[0] and a[1] >= b[1] and a[2] >= b[2]) #if x skilll score is greater than b and x skill score is grreater than z then return the 1st person i.e. x
    f2=(a[0] > b[0] or a[1] > b[1] or a[2] > b[2]) #if any score is greter than other members then retrun that member
    return f1 and f2
for _ in range(int(input())): #looping through the skills of team members
    x=list(map(int,input().split())) #x score
    y=list(map(int,input().split())) #y score
    z=list(map(int,input().split())) #z score
    if result(x,y) and result(y,z): #if anyone is greater than other print yes
        print("yes")
    elif result(x,z) and result(z,y): #comparing z
        print("yes")
    elif result(y,x) and result(x,z):
        print("yes")
    elif result(y,z) and result(z,x):
        print("yes")
    elif result(z,x) and result(x,y):
        print("yes")
    elif result(z,y) and result(y,x): #comparing y
        print("yes")
    else:
        print("no") #if such order doesn't exists
