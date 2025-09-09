num_list = []
total = 0

for i in range (9) :
    num = int(input())
    num_list.append (num)
    total += num

num_list.sort()

found = False
for i in range (9) : 
    for j in range(i+1,9):
        if num_list[i]+num_list[j] == total -100 :
            fake1, fake2 = num_list[i], num_list[j]
            num_list.remove(fake1)
            num_list.remove(fake2)
            found = True
            break
    if found:
        break 

for num in num_list:
    print(num)