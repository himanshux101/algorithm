arr = [6, 5, 4, 3 ,2, 1]

COUNT = 0

def count_split(a, b):
    # merge two arrays
    c = []
    i = j = 0
    n1 = len(a)
    n2 = len(b)

    inter = 0

    while i < n1 and j < n2:
        if a[i] < b[j]:
            c.append(a[i])
            i += 1
        elif b[j] < a[i]:
            c.append(b[j])
            # add the remaining elements in array1 
            inter = inter + n1 - i
            j += 1

    while i < n1:
        c.append(a[i])
        i += 1

    while j < n2:
        c.append(b[j])
        j += 1

    return c, inter

def count(arr):
    n = len(arr)
    half = int(n/2)

    if n == 1:
        return arr

    a = count(arr[:half])
    b = count(arr[half:])

    c, inter = count_split(a, b)

    global COUNT
    COUNT = COUNT + inter

    return c

def count_inversions(arr):
    count(arr)
    return COUNT

