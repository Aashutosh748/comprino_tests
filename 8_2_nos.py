'''
1. take 2 nos.
2. bob turn.
3. alice turn.
4. turm till the no of chances loop.
5. find max min.
'''

x = int(input()) #taking 2 nos
for i in range(x):  #in the nos turns
    a, b, n = map(int, input().split()) #spliting nos in turns
    if n % 2 == 1: #bob turn
        a *= 2 #alice multiply by 2
    print(max(a, b) // min(a, b)) #find min max
