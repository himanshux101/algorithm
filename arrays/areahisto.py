height = [2,1,5,6,2,3]


height.append(0)
stack = [-1]
print(stack)
ans = 0
for i in range(len(height)):
    print('--------i is -> ', i)
    while height[i] < height[stack[-1]]:
        h = height[stack.pop()]
        print('height of current ', h)
        w = i - stack[-1] - 1
        print(i, stack, w)
        ans = max(ans, h * w)
        print('ans is ', ans, h*w, h, w)
    print('stack -> ', stack, stack[-1])
    stack.append(i)
    print('after stack -> ', stack, stack[-1])
height.pop()
print('ansns ', ans)
# def find_area(hist):
#     if len(hist) == 2:
#         pass
#     global_max = 0
#     minimum = min(hist)
#     min_index = hist.index(minimum)

#     area = len(hist) * minimum
#     if area > global_max:
#         global_max = area
#     if len(hist) == 2:
#         if hist[0] > global_max:
#             global_max = hist[0]
#         if hist[1] > global_max:
#             global_max = hist[1]
    
#     if len(hist) > 2:
#         max_left = find_area(hist[:min_index]) 
#         if max_left > global_max:
#             global_max = max_left
        
#         max_right = find_area(hist[min_index+1:])
#         if max_right > global_max:
#             global_max = max_right
#     return global_max

# consider when the height is the only single histogram 

# print(find_area(hist))
