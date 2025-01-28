count = int(input())
ans = 0
for _ in range(count):
    a = input().split(' ')
    total = sum(map(int, a))
    if total > 1:
        ans += 1
print(ans)