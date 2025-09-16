n = int(input())
arr = list(map(int, input().split()))

money1 = n #현재 남은 돈
money2 = n
stock1 = 0
stock2 = 0

for i in range (14):
    if money1 >= arr[i]: #살 수 있을 때
        stock1 = stock1 + money1//arr[i]
        money1 = money1%arr[i]


for i in range (14):
    if i>=3 :
        #3일째 연속 상승시 전량 매도
        if arr[i-3]<arr[i-2] and arr[i-2]<arr[i-1] and arr[i-1]<arr[i]:
            money2 += stock2*arr[i]
            stock2 = 0
            #print("3일 연속 주가 상승!")
            #print("3일간 주가 흐름 ", arr[i-2], arr[i-1], arr[i])
        #3일째 연속 하락시
        elif arr[i-3]>arr[i-2] and arr[i-2]>arr[i-1] and arr[i-1]>arr[i] :
            if money2 >= arr[i]:
                stock2 = stock2 + money2//arr[i]
                money2 = money2%arr[i]
    
    #print("현재 남은 돈", money2)
    #print("현재 보유 주식", stock2)
    #print("---------")

result1 = arr[13]*stock1 + money1
result2 = arr[13]*stock2 + money2


if result1 > result2:
    print("BNP")
elif result1 == result2 :
    print("SAMESAME")
elif result1 < result2 :
    print("TIMING")