public class Solution {
    public int[] TwoSum(int[] nums, int target) {
        var dict = new Dictionary<int, int>();

        
        for (var i = 0; i < nums.Length; i++) {       
            if (dict.TryGetValue(nums[i], out var x))
                return new[] {i,x };
            
            dict[target - nums[i]] = i;
        }
        
        return null;
    }
}
