arr = [ [2, 5, 6, 8], [1, 4, 5, 6, 10], [4, 5, 6, 7]]

common = set(arr[0]).intersection(set(arr[1]))

for i in range(3, len(arr)):
    common = common.intersection(set(arr[i]))

print('common is ', common)
    