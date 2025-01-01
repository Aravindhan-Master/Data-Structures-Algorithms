def partition(nums: list, left: int, right: int):
    i = left - 1
    pivot = nums[right]

    for j in range(left, right):
        if nums[j] < pivot:
            i += 1
            nums[i], nums[j] = nums[j], nums[i]

    nums[i+1], nums[right] = nums[right], nums[i+1]

    return i + 1

def quick_sort(nums: list, left: int, right: int):
    if left < right:
        p = partition(nums, left, right)
        quick_sort(nums, left, p-1)
        quick_sort(nums, p+1, right)


num_list = [10, 4, 6, 2, 1, 7, 3, 5]

quick_sort(num_list, 0, len(num_list)-1)
