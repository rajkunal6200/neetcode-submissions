class Solution:
    def rob(self, nums: list[int]) -> int:
        if len(nums) == 1:
            return nums[0]
            
        def rob(houses):
            prev2 = 0
            prev1 = 0

            for money in houses:
                current = max(prev1, prev2 + money)
                prev2 = prev1
                prev1 = current
            return prev1
            
        return max(rob(nums[:-1]), rob(nums[1:]))
