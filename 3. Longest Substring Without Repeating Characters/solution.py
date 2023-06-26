from collections import OrderedDict

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
                
        m = OrderedDict()
        output = 0
        for x in s:
            
            while (x in m):
                todel = next(iter(m))
                del m[todel]
               
                
            m[x] = None
            l = len(m)
            output = max(output, l)
        
        return output
