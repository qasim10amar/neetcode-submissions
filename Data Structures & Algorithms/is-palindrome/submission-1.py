class Solution:
    def isPalindrome(self, s: str) -> bool:
        lower_s = s.lower()
        
        cleaned = [char for char in lower_s if char.isalnum()]
        
        l = 0
        r = len(cleaned) - 1

        while l < r:
            if cleaned[l] == cleaned[r]:
                l += 1
                r -= 1
            else:
                return False
        return True

        