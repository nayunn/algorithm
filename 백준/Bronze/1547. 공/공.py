m = int(input())

cup =[1,0,0]

for i in range (m):
    move1, move2 = map(int, input().split())
    if cup[move1-1]==1 or cup[move2-1]==1:
        if cup[move1-1] ==1:
            cup[move1-1] = 0
            cup[move2-1] = 1
        else: 
            cup[move2-1] = 0
            cup[move1-1] = 1

for i in range (len(cup)):
    if cup[i] ==1:
        print(i+1)
        break