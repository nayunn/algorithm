m = int(input())

cup =[1,0,0]

for i in range (m):
    move1, move2 = map(int, input().split())

    #print("시도 : " , i+1) #확인용 코드
    
    if cup[move1-1]==1 or cup[move2-1]==1:
        cup[move1-1], cup[move2-1] = cup[move2-1], cup[move1-1]

    ''' 
    #확인용 코드       
    for j in range(len(cup)):
        if cup[j] == 1:
            print("현재 공 위치 : ", j+1 )
            print (cup) '''

for i in range (len(cup)):
    if cup[i] ==1:
        print(i+1)
        break