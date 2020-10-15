nums = [3,7,2,24,12,1,5,6,4,9,13,10,25]
nums = [ i*i for i in nums]
nums.sort()
print(nums)

count = 0
for i in range(len(nums)-1, 0, -1):
    num = nums[i]
    a = 0
    b = i - 1
    while a < b:
        if nums[a] + nums[b] == num:
            count += 1
            break
        elif nums[a] + nums[b] < num:
            a += 1
        else:
            b -= 1

print(count)