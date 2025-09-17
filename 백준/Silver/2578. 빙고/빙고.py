import sys
bingo = [list (map(int,input().split())) for _ in range(5)]
nums = [x for _ in range(5) for x in map(int,input().split())]

def check_bingo(checking):
    point = 0
    #행에 대해 체크
    for i in range(5):
        if all(row==0 for row in checking[i]):
            point+=1
    #열에 대해 체크
    for j in range(5):
        if all(checking[i][j]==0 for i in range(5)):
            point+=1
    #대각선 y=-x
    if checking[0][0]==checking[1][1]==checking[2][2]==checking[3][3]==checking[4][4]==0 :
        point+=1
    #대각선 y=x
    if checking[4][0]==checking[3][1]==checking[2][2]==checking[1][3]==checking[0][4]==0:
        point+=1
    return point

for x in range(25):
    for i in range(5):
        for j in range(5):
            if nums[x] == bingo[i][j]:
                bingo[i][j] = 0
                if check_bingo(bingo) >= 3 :
                    print(x+1) 
                    sys.exit()