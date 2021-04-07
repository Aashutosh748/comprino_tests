'''
1. take the array.
2. take the numbers.
3. check the multiplication of the nos.
4. if one is there then return the no.
5. if one is there and other is not there then return.
6. other is present but former no is not present.
7. check the conditions.
8. if presnt then yes.
9. else no.
'''


numCase = int(input()) #input 
for i in range(numCase): #inside the array
    length = int(input()) #array size
    array = [int(x) for x in input().split(' ')] #array elements
    num_neg_ones = len([x for x in array if x == -1]) #if the 1st no is in the array
    num_ones = len([x for x in array if x == 1]) #if the no is in the size of array
    num_other = len([x for x in array if x not in [0, -1, 1]]) #if no is out of scope

    answer = "yes" #if present boolean set yes
    if num_other > 1: #if both no not present
        answer = "no" #set to no
    if num_other == 1 and num_neg_ones > 0: #if one is presnet and other is not prsent
        answer = "no"
    if num_neg_ones > 1 and num_ones == 0: #if 1st no is not present and other is present
        answer = "no"
    print(answer)
