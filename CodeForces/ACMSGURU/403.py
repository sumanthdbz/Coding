import math
def solve(a, b, c):
    p1 = b**2 #b^2
    p2 = 4*a*c #-4ac
    ans = int(math.sqrt((p1 + p2)))
    ans -= b
    return ans//2 + 1

RHS_b = 2
RHS_c = 2
multiplier = int(input())
RHS_b *= multiplier
RHS_c *= multiplier
fin_a = 1
fin_b = 1 - RHS_b

print(solve(1, fin_b, RHS_c))