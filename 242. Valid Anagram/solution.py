class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
           return False
        
        s1 = [*s]
        t1 = [*t]
        s1.sort()
        t1.sort()
        
        
        for x,y in itertools.zip_longest(s1, t1):
            if y != x:
                return False
        
        return True
