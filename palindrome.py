class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        if x%10 == 0 and x != 0:
            return False
        rev = 0
        o = x
        c = 0
        while x > rev:
            rev = rev * 10 + x%10
            x//=10
        return x == rev or x == rev//10
        

print(Solution().isPalindrome(1221)) # True
print(Solution().isPalindrome(12321)) # True