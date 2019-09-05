a1 = [1, 3, 5, 7]
a2 = [2, 4 ,6 ,8]

arr = [4, 5, 2, 1, 7, 3, 8, 6]

def merge(a, b):
    # merge two arrays
    c = []
    i = j = 0
    n1 = len(a)
    n2 = len(b)

    while i < n1 and j < n2:
        if a[i] < b[j]:
            c.append(a[i])
            i += 1
        elif b[j] < a[i]:
            c.append(b[j])
            j += 1

    while i < n1:
        c.append(a[i])
        i += 1

    while j < n2:
        c.append(b[j])
        j += 1

    return c

def merge_sort(arr):
    # print('one')
    n = len(arr)
    half = int(n/2)

    if n == 1:
        return arr

    a = merge_sort(arr[:half])
    b = merge_sort(arr[half:])

    return merge(a, b)


print(merge_sort(arr))
