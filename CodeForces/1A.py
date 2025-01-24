import math
n, m, a = map(int, input().split())

c1 = math.ceil(n/a)
c2 = math.ceil(m/a)
print(c1 * c2)