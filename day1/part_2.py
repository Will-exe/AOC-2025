
a1 = []

with open('input.txt', 'r') as file:
    lines = file.readlines()
   # print(lines)
    for line in lines:
        a1.append(line.strip())
        

#a1.sort()
value = 0
dir = 'r'
sum = 50
count = 0
prevSum = 50


for x in range(len(a1)):
    skipFlag = False
    dir = a1[x][0]    
    value = a1[x][1:]
   
    #print("test dir :", dir)
    #print("test val :", value)
    if dir == 'R' :
        sum += int(value)
    else:
        sum -= int(value)
    
    if sum % 100 == 0 and len(str(abs(sum))) > 2:
        skipFlag = True
    count += abs(sum) // 100
    if sum < 0:
        if prevSum != 0:
            count += 1
        sum += 100
    sum = sum % 100

    prevSum = sum
    if sum == 0 and skipFlag == False:
        count += 1
    
    print("test a1 :", a1[x])
    print(sum)
    print("count: ", count)
    print()



print("count: ", count)


