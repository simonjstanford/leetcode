class Solution:
    def isPalindrome(self, s: str) -> bool:
        import re
        s1 = re.sub("[^a-zA-Z0-9]", '', s).lower()
        s2 = s1[::-1]
        return s1 == s2
