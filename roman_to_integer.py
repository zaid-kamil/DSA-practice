class Solution:
    def romanToInt(self, s: str) -> int:
        map = {
            'I' : 1, 'V': 5, 'X': 10, 'L': 50, 'C':100, 'D': 500, 'M':1000
        }
        ans = 0
        prev = 0
        for c in s[::-1]:
            curr = map[c]
            if curr < prev:
                ans -= curr
            else:
                ans += curr
            prev = curr
        return ans
    

print(Solution().romanToInt("LVIII"))
print(Solution().romanToInt("MCMXCIV"))
print(Solution().romanToInt("III"))
