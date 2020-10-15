nums = [1,2,3,4,0,0,4,0]
i = len(nums) - 1 
swap = 0

while i > 0:
    if nums[i] == 0:
        swap += 1
        print('swap is', swap)
    else:
        nums[i], nums[i-swap] = nums[i-swap], nums[i]
    i -= 1

print(nums)