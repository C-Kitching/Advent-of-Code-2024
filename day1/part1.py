

list1 = []
list2 = []

with open("./day1/input.txt", "r") as file:
    for line in file:
        num1, num2 = map(int, line.split())
        list1.append(num1)
        list2.append(num2)

list1.sort()
list2.sort()


res = 0
for i in range(len(list1)):
    res += abs(list1[i]-list2[i])

print(res)