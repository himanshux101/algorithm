arr = [6, 7, 4, 3, 2, 1, 4, 5]

def peak(arr, l, r):
    if r - l == 0:
        return l

    mid = l + (r - l)/2
    mid = int(mid)

    if arr[mid] > arr[mid-1] and arr[mid] > arr[mid+1]:
        return mid
    elif arr[mid] < arr[mid-1]:
        return peak(arr, l, mid-1)
    else:
        return peak(arr, mid+1, r)

print(peak(arr, 0, len(arr)-1))
