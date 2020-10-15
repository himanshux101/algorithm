import math 

a = [1,2,3,4,5,6,7,8,9,10]

def search(arr, val):
    length = len(arr)
    if length > 0:
        mid =  (length - 1) / 2
        mid = math.floor(mid)
        if arr[mid] == val:
            return "found"
        elif arr[mid] > val:
            return search(arr[:mid], val)
        elif arr[mid] < val:
            return search(arr[mid+1:], val)
    else:
        return False

var = search(a, 2)
print(var)