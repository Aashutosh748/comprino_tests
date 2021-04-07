'''
1. take the salary .
2. fins the intrest by the formula.
3. calculate the gross salary.
4. print the salary 
'''

for _ in range(int(input())): # in total salary 
    n=int(input()) #salary amount
    salary=0 
    if n<1500: # if amount is greater than 1500
        salary=n*2 #multiply by 2
    else: # else other intrests
        salary=n*1.98+500
    print(salary) #final salary
