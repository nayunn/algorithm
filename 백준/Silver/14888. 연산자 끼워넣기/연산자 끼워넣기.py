from itertools import permutations

n = int(input())
nums = list(map(int,input().split()))
ops = list(map(int,input().split()))
Ops = []
for i in range(ops[0]):
    Ops.append('+')
for i in range(ops[1]):
    Ops.append("-")
for i in range(ops[2]):
    Ops.append("*")
for i in range(ops[3]):
    Ops.append("//")


cases = set(permutations(Ops, n-1))

def calc(nums, case):
    result = nums[0]
    for i in range(n-1):
        if case[i]=='+':
            result+=nums[i+1]
        elif case[i]=='-':
            result-=nums[i+1]
        elif case[i]=='*':
            result*=nums[i+1]
        elif case[i]=='//':
            if result >=0 :
                result//=nums[i+1]
            else:
                result=-(-result//nums[i+1])
    return result

minv=10**9
maxv=-10**9

for case in cases:
    val = calc(nums, case)
    maxv = max(maxv, val)
    minv = min(minv, val)

print(maxv)
print(minv)