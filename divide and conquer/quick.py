import random
import math

compare = 0

def choosePivot(arr, l, r, pivot):
    if pivot == 'first':
        return 
    if pivot == 'last':
        arr[l], arr[r] = arr[r], arr[l]
    if pivot == 'median':
        first = arr[l]
        last = arr[r]
        n = r - l + 1
        # print(n)
        if n % 2 == 0:
            m = int(n / 2)
            # print('first')
        else: 
            m = int(math.ceil(n / 2))
            # print('second')

        # print('this is m : ' + str(m))

        mid = arr[l + m - 1]

        if ((first < mid and mid < last) or (last < mid and mid < first)):
            # print('choose middle one : ' + str(mid))
            arr[l], arr[l + m - 1] = arr[l + m - 1], arr[l]
        elif ((mid < first and first < last) or (last < first and first < mid)):
            # print('choose first one : ' + str(first))
            return  
        else:
            # print('choose last one : ' + str(last))
            arr[l], arr[r] = arr[r], arr[l]



def partition(arr, l, r):
    pivot = arr[l]
    i = l + 1

    for j in range(l+1, r+1):
        if arr[j] < pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[l], arr[i-1] = arr[i-1], arr[l]
    return i-1

def quickSort(arr, l, r, pivot):
    if r - l + 2 == 1:
        return

    choosePivot(arr, l, r, pivot)

    i = partition(arr, l, r)
    # compare r - l times
    global compare
    compare = compare + r - l

    quickSort(arr, l, i-1, pivot)
    quickSort(arr, i+1, r, pivot)


# size = 10000 
# array = [random.randrange(10000) for i in range(size)]
# quickSort(array, 0, size-1)

isSorted = lambda arr: all(arr[i] <= arr[i+1] for i in range(len(arr)-1))

with open('QuickSort.txt') as file:
	lines = file.readlines()

lines = [int(line.rstrip('\n')) for line in lines]
size = len(lines)
quickSort(lines, 0, size-1, 'median')
print(isSorted(lines))
print(compare)

# test = [7, 2, 10, 5, 7, 10, 4, 7, 7, 9, 99]
# print(test)
# choosePivot(test, 0, 10, 'median')
# print(test)