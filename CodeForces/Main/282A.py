count = int(input())
total = 0
for _ in range(count):
    cmd = input()
    if '+' in cmd:
        total += 1
    else:
        total -= 1
print(total)