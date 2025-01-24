n, k = map(int, input().split())
nums = list(map(int, input().split()))

ans = k
score = nums[k-1]
if score == 0:
    modded_arr = nums[:k]
    for i in modded_arr[::-1]:
        if score == i:
            ans -= 1
        else:
            break
else:
    for i in nums[k:]:
        if score == i:
            ans += 1
        else:
            break
print(ans)