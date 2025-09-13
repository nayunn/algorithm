n,m = map(int,input().split())

arr = []
for i in range (n):
    line = input().strip()
    row = list(line)
    arr.append(row)

mismatch = 65

for i in range (n-7):
    for j in range (m-7):
        count1 =0 #w시작
        count2 =0 #b시작
        for x in range (i,i+8):
            for y in range (j, j+8):
                if (x+y)%2==0:
                    expected1 = 'W'
                    expected2 = 'B'
                else:
                    expected1 = 'B'
                    expected2 = 'W'
                if arr[x][y] != expected1:
                    count1 +=1
                if arr[x][y] != expected2:
                    count2 +=1

        curr_min = min(count1,count2)
        if curr_min < mismatch:
            mismatch = curr_min

print(mismatch)