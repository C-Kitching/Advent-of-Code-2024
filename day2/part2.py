def is_safe(report, allowed_issues):
    # Check if the report is strictly increasing or decreasing
    increasing = all(0 < report[i] - report[i-1] <= 3 for i in range(1, len(report)))
    decreasing = all(0 < report[i-1] - report[i] <= 3 for i in range(1, len(report)))

    if increasing or decreasing:
        return True

    if allowed_issues > 0:
        # Try removing each level and check if the resulting sequence is safe
        for i in range(len(report)):
            modified_report = report[:i] + report[i+1:]
            if is_safe(modified_report, allowed_issues - 1):
                return True

    return False

res = 0

with open("./day2/input.txt", "r") as file:
    for line in file:
        report = list(map(int, line.split()))
        if is_safe(report, 1):  # Allow removing one bad level
            res += 1

print(res)
