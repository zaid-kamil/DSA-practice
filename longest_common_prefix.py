from typing import List, Iterable

# Time complexity O(m * n)
# Space complexity O(n)
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        lcp = ""
        for item in zip(*strs):
            if are_same(item):
                lcp+=item[0]
            else:
                break
        return lcp
def are_same(items: Iterable[str])->str:
    return all(item == items[0] for item in items)
    
# Time complexity O(n log n + m)
# Space complexity O(n)
# The new implementation is generally better 
# in terms of time complexity, especially 
# when the number of strings (n) is large.
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        lcp = ""
        if not len(strs): return lcp
        strs = sorted(strs)
        for i in zip(strs[0], strs[-1]):
            if not i[0] == i[-1]:
                break
            lcp += i[0]
        return lcp


print(Solution().longestCommonPrefix(["flower","flow","flight"]))
print(Solution().longestCommonPrefix(["dog","racecar","car"]))
