count = int(input())
for _ in range(count):
    a = input()
    if len(a) < 11:
        print(a)
    else:
        print(a[0], len(a)-2, a[-1], sep='')