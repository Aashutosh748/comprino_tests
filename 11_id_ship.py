'''
1. input the ship , id
2. compare the ship id
3. print according to id
'''

n=int(input()) #ship id
for i in range(0,n): #go through the list
    a=input() # ship
    if(a=='B' or a=='b'): #if b then battelship
        print("BattleShip")
    elif(a=='C' or a=='c'): #comparison
        print("Cruiser")
    elif(a=='D' or a=='d'): #comparison
        print("Destroyer")
    elif(a=='F' or a=='f'): #comparison
        print("Frigate") #print result
    
