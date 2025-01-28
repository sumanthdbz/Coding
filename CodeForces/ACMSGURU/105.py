def calc_digit_sum(x):
    total = 0
    if x < 10:
        return x
    while x:
        total += x%10
        x //= 10
    if total%3 == 0:
        total = 0
    return total

total = 0
counter = 0
n1 = int(input())
for i in range(1, n1 + 1):
    total += calc_digit_sum(i)
    if total%3 == 0:
        counter += 1
        total = 0
print(counter)