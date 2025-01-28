n, m = 0, 0
for i in range(5):
    a = input().split()
    if '1' in a:
        n = i
        m = a.index('1')

ans = abs(n-2) + abs(m-2)
print(ans)