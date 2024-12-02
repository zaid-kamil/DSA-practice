from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        store = {}
        for i in range(len(nums)):
            c = target - nums[i]
            if c in store:
                return store[c], i
            else:
                store[nums[i]] = i
        return []
        
        


s = Solution()
print(s.twoSum([2,7,11,15], 9)) # [0, 1]
print(s.twoSum([3,2,4], 6)) # [1, 2]
print(s.twoSum([3,3], 6)) # [0, 1]
print(s.twoSum([3,3,1,2,4,5,5,1,2,2,5,5,1,45,56,5,1,2], 11)) # []