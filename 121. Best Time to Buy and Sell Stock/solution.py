class Solution:
    def maxProfit(self, prices: List[int]) -> int:
      
       min_p = prices[0]
       max_p = 0
       for p in prices:
            min_p = min(min_p, p)
            max_p = max(max_p, p-min_p)
            
            
       return max_p
