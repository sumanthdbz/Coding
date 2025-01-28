a, b = 0, 1
k = int(input())
ans = 0
for _ in range(k):
    c = a + b
    a = b
    b = c
    ans += a
print(ans)