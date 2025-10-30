n1 = int(input())
ans = n1//3 * 2
rem = 0
if n1%3 == 1:
    rem = 0
elif n1%3 == 2:
    rem = 1

ans += rem
print(ans)