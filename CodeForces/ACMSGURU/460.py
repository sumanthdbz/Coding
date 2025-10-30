x = int(input())
for _ in range(x):
    n = input()
    ans = None
    last_char = n[-1]
    if last_char in ['x', 's', 'o', 'h']:
        if len(n) > 1 and last_char == 'h':
            if n[-2] == 'c':
                ans = n + 'es'
        else:
            ans = n + 'es'
    elif last_char == 'e':
        if n[-2] == 'f':
            ans = n[:-2] + 'ves'
        else:
            ans = n + 's'
    elif last_char in ['y']:
        ans = n[:-1] + 'ies'
    else:
        ans = n + 's'

    print(ans)