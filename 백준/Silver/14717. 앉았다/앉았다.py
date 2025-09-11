n1, n2 = map(int, input().split())
deck = [1,2,3,4,5,6,7,8,9,10,1,2,3,4,5,6,7,8,9,10]
deck.remove(n1)
deck.remove(n2)
win = 0

def rank(a,b):
    if a==b:
        return (1, a)
    else:
        return (0, (a+b)%10)

my_rank = rank(n1,n2)
#print(my_rank)

for i in range (len(deck)):
    for j in range (i+1,len(deck)):
        op_rank = rank(deck[i], deck[j])
        if my_rank > op_rank:
            win +=1

print(f"{win/153:.3f}") #18C2 = 153