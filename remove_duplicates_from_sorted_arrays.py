from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums: return 0
        i = 0
        for j in range(1, len(nums)):
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]
        return i+1



# Example usage
# print("----"*5)
print(Solution().removeDuplicates([1,1,2])) # 2
print("----"*5)
print(Solution().removeDuplicates([1,1,1,1,1,1,2,2,2,2,2,2,2,2,2])) # 5
# print("----"*5)
print(Solution().removeDuplicates([1,2,3])) # 3



