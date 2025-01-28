def calc_gcd(n1, n2):
    coprime = True
    gcd = 0
    while True:
        gcd = n1 % n2
        if gcd == 0:
            coprime = False
            break
        if gcd == 1:
            break
        n1 = n2
        n2 = gcd
    return coprime

n1 = int(input())
counter = 1
for i in range(2, n1):
    if calc_gcd(i, n1):
        counter += 1
print(counter)