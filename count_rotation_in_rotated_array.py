def binary_search(nums):
    lo = 0
    hi = len(nums) -1
    # if the array is not rotated
    if nums[lo] < nums[hi]:
        return 0
    # if the array is rotated
    while lo <= hi:                                # while the left index is less than or equal to the right index
        mid = (lo + hi) // 2                       # get the middle index
        if mid > 0 and nums[mid] < nums[mid-1]:    # if the middle index is greater than 0 and the middle index is less than the middle index - 1
            return mid                             # return the middle index                          
        elif mid < nums[hi]:                       # if the middle index is less than the right index
            hi = mid - 1                           # set the right index to the middle index - 1
        else:                                      # otherwise                 
            lo = mid + 1                           # set the left index to the middle index + 1


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

