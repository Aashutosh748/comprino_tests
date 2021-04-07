'''
1. choose sticks.
2. take the area.
3. count no of sticks so that none are broken.
4. matche the max area.
5. for a rectangle at least 4 sticks is reqd.
6. yes if area present.
'''

for _ in range(int(input())): #total no of sticks
    n = int(input())
    a1 = list(map(int, input().split()))
    a2 = list(set(a1))
    a3 = []
    for i in a2:  #choosing sticks
        c = a1.count(i)
        if c % 2 == 0: #total area 
            a3 += [i for _ in range(c)]
        elif c > 1:
            a3 += [i for _ in range(c - 1)]
    if len(a3) == 2: #if area matches
        print(-1)
    else:
        c = max(a3) #if sticks ok
        mx1 = a3.pop(a3.index(c)) #forming the stuck, area and length
        a3.remove(c)
        c = max(a3)
        mx2 = a3.pop(a3.index(c)) #for a rectangle area at least 4 sticks are reqd
        print(mx1 * mx2)
        
