class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        
        if len(nums) < 3 or nums[0] > 0 or nums[-1] < 0:
            return[]
           
        for i in range(len(nums) -2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
                
            target = 0 - nums[i]
            L = i + 1
            R = len(nums) -1
            
            while L < R:
                sumNow = nums[L] + nums[R]
                if sumNow < target:
                    L += 1
                elif sumNow > target:
                    R -= 1
                else:
                    x = [nums[i], nums[L], nums[R]]
                    result.append(x)                         
                    while (L < R and nums[R-1] == nums[R]): R -= 1
                    R-=1
                    L+=1
        
        return result
