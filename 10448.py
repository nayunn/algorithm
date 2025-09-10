n = int(input())
K = [int(input()) for _ in range(n)]

maxK = max(K)
samgak = []

#삼각수 미리 만들어놓음
for i in range (1,maxK):
    t = i*(i+1)//2
    if t > maxK:
        break
    samgak.append(t)

def can_make(k):
    for i in range (len(samgak)):
        if k < samgak[i]:
            break
        for j in range (len(samgak)):
            for z in range (len(samgak)):
                if samgak[i] + samgak[j] + samgak[z] == k:
                    print(1)
                    return
    print(0)               

for i in range (len(K)):
    can_make(K[i])