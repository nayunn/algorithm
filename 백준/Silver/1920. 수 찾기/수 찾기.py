n = int(input())
arrn = list(map(int,input().split()))
m = int(input())
arrm = list(map(int,input().split()))

arrn.sort()

def BinSearch(arr, target, left, right):
    if target > arrn[n-1]:
        return 0
    elif target < arrn[0]:
        return 0
    

    if left > right:
        return 0
    mid = (left+right)//2

    if arr[mid] == target:
        return 1
    elif arr[mid] > target:
        return BinSearch(arr, target, left, mid-1)
    elif arr[mid] < target:
        return BinSearch(arr, target, mid+1, right)
    
for i in range(m):
    print(BinSearch(arrn, arrm[i], 0, n-1))