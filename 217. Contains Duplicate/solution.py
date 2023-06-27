class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        tmp = set()
        for n in nums:
            if n in tmp:
                return True
            else:
                tmp.add(n)
        return False
        
