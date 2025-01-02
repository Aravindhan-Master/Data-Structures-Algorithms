def partition(arr, left, right):
    i = left - 1
    pivot = arr[right]

    for j in range(left, right):
        if arr[j] < pivot:
            i += 1
            arr[j], arr[i] = arr[i], arr[j]

    arr[i+1], arr[right] = arr[right], arr[i+1]

    return i+1

def k_smallest(arr, k, left, right):
    if left < right:
        p = partition(arr, left, right)

        if p > k:
            k_smallest(arr, k, left, p-1)

        else:
            k_smallest(arr, k, p+1, right)

    return arr[k]

arr = [2, 3, 6, 5, 8, 7, 4, 1, 9]
k = 8

ele = k_smallest(arr, k-1, 0, len(arr)-1)

print(ele)
