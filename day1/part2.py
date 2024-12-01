
import collections
from collections import Counter

list1 = []
list2 = []

with open("./day1/input.txt", "r") as file:
    for line in file:
        num1, num2 = map(int, line.split())
        list1.append(num1)
        list2.append(num2)

count = Counter(list2)

similarity = 0

for num in list1:
    if num in count.keys():
        similarity += num*count[num]

print(similarity)