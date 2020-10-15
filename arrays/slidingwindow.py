# nums = [1,3,-1,-3,5,3,6,7]
nums = [1,3,1,2,0,5]
k = 3

from collections import deque 

def sliding(nums, k):
    deq = deque()
    ans = []
    if not nums:
        return 0

    for i in range(k):
        while deq and nums[deq[-1]] < nums[i]:
            deq.pop()
        deq.append(i)
    
    ans.append(nums[deq[0]])
    
    for i in range(k, len(nums)):
        while deq and deq[0] < i - k + 1:
            deq.popleft()
        while deq and nums[deq[-1]] < nums[i]:
            deq.pop()
        deq.append(i)
        ans.append(nums[deq[0]])
    
    print(ans)

    return ans


sliding(nums, k)