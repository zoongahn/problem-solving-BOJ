import sys

input = sys.stdin.readline

subject_total = 20
rate_list = []
total_rate = 0
total_credit = 0

for _ in range(subject_total):
    subject, credit_, rate_str = input().strip().split()
    credit = float(credit_)
    rate = 0.0
    if rate_str == "P":
        continue
    match (rate_str[0]):
        case "A":
            rate += 4
        case "B":
            rate += 3
        case "C":
            rate += 2
        case "D":
            rate += 1
    if len(rate_str) > 1 and rate_str[1] == "+":
        rate += 0.5

    total_rate += (rate * credit)
    total_credit += credit

print(total_rate / total_credit)
