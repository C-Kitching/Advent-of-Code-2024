
def is_safe(report):

    if report[-1] < report[0]:
        report.reverse()

    for i in range(1, len(report)):
        if report[i] <= report[i-1] or report[i] - report[i-1] > 3:
            return False
        
    return True

res = 0

with open("./day2/input.txt", "r") as file:

    for line in file:

        report = list(map(int, line.split()))

        if is_safe(report): 
            res += 1

print(res)