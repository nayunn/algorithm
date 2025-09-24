import sys
input = sys.stdin.readline  

n = int(input())
arrn = list(map(int, input().split()))

m = int(input())
arrm = list(map(int, input().split()))

count = {}
for num in arrn:
    count[num] = count.get(num, 0) + 1 

result = []
for num in arrm:
    result.append(str(count.get(num, 0)))

print(" ".join(result))
