nums = [3, 6, 1, 5, 10, 2, 9]

for i in range(1, len(nums)):
    prev = i - 1
    current = i
    while nums[current] < nums[prev] and prev >= 0 and current >= 0:
        nums[current], nums[prev] = nums[prev], nums[current]
        prev -= 1
        current -= 1
