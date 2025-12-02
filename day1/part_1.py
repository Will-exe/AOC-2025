
a1 = []

with open('input.txt', 'r') as file:
    lines = file.readlines()
   # print(lines)
    for line in lines:
        a1.append(line.strip())
        

#a1.sort()
value = 0
dir = 'r'
print(a1)
sum = 50
count = 0
print(sum)

for x in range(len(a1)):
    dir = a1[x][0]    
    value = a1[x][1:]
   
    #print("test dir :", dir)
    #print("test val :", value)
    if dir == 'R' :
        sum += int(value)
    else:
        sum -= int(value)
    if sum < 0:
        sum += 100
    sum = sum % 100

    print("test a1 :", a1[x])
    print(sum)
    print()

    if sum == 0:
        count += 1
    


print("count: ", count)
