n,m = map(int, input().split())
#딕셔너리 사용하자
dic = {}
for i in range(n):
    name = input()
    dic[i+1] = name
    dic[name] = i+1

for i in range(m):
    mm = input()
    if mm.isdigit():
        print(dic[int(mm)])
    else:
        print(dic[mm])