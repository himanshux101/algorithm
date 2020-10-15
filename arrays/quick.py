# a = [5,1,1,2,0,0]
a = [10, 80, 30, 90, 40, 50, 70]

def quickSort(arr, low, high):
    if low < high:
        p = partition(arr, low, high) # partition it 
        print(arr)
        # to the left 
        quickSort(arr, low, p)
        # to the right 
        quickSort(arr, p+1, high)

def partition(a, low, high):
    pivot = a[low]

    i = low + 1 
    for j in range(low+1, high):
        if a[j] < pivot:
            a[j], a[i] = a[i], a[j]
            i += 1
    a[low], a[i-1] = a[i-1], a[low]
    return i-1

print(a)
quickSort(a, 0, len(a))
print(a)