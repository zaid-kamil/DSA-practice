def binary_search(nums):
    lo = 0
    hi = len(nums) -1

    while lo <= hi:
        mid = (lo + hi) // 2
        if mid > 0 and nums[mid] < nums[mid-1]:
            return mid
        elif mid < nums[hi]:
            hi = mid - 1
        else:
            lo = mid + 1
    return 0



nums = [8,9,10,1,2,3,4,5,6,7] # 3
value = binary_search(nums)
print(f'Rotation: {value}')
nums = [4,5,6,7,8,9,10,1,2,3] # 7
value = binary_search(nums)
print(f'Rotation: {value}')

nums = [1,2,3,4,5,6,7,8,9,10] # 0
value = binary_search(nums)
print(f'Rotation: {value}')
nums = [2,3,4,5,6,7,8,9,10,1] # 9
value = binary_search(nums)
print(f'Rotation: {value}')

