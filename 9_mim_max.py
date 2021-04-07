'''
1. take nos in a list.
2. split the list.
3. store the no in array.
4. find min fo ral theh nos by loop.
5. print the nos.
'''

for _ in range(0,int(input())): #in the lists
    n=int(input()) #input the nos
    arr=list(map(int,input().split()))  #split no in the list
    minn=min(arr) #finding min of the nos
    print(minn*(n-1)) #print
