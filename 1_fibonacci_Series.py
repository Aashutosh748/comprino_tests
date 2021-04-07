tat'''Pseudo code:
1. take input from user string.
2. create lists to hold the strings.
3. create empty list to hold the answer.
4. fill the strings sets in the s1.
5. sort the string.
6. check if the string is less than 3.
7. if less than 3 then dynamic.
8. check fibbonacci series.
9. If permutation satisfies in series then Dynamic.
10. if not permutation in series then Not.

'''


for _ in range(int(input())): #input for the strings
    s=input() #string
    s2=list(s) #list contatining string
    s1=list(set(s)) #list contatining string sets to match
    a=[] #empty list to hold answer
    for i in s1: # itirating the string in s1
        a.append(s2.count(i)) #adding the strings to s1
    a=sorted(a) #sorting the string
    if(len(a) < 3): #if c1,c2,c3 less than 3 then dynamic
        print("Dynamic") 
    else: #if not less than 3
        for i in range(len(a)-1, 1, -1): #checking the strings
            if a[i] == a[i-1] + a[i-2]: #fibonacci series checker
                print("Dynamic") #if fibonacci series then dynamic
                break
            else: #if not in series pattern
                print("Not") #not dynamic
                break
