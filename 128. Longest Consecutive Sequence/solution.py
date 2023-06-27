class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        nums.sort()
        max_length = 1
        previous = nums[0]
        count = 1
        
        for n in nums[1:]:
            if n == previous:
                continue
            elif n == (previous + 1):
                count += 1
            else:
                count = 1
            
            if count > max_length:
                max_length = count
                
            previous = n
            
        return max_length
            
