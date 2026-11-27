from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        subset = []

        def dfs(i):
            if i == len(nums):
                result.append(subset.copy())
                return
            
            # Decision 1: Include nums[i]
            subset.append(nums[i])
            dfs(i + 1)
            
            # Decision 2: Exclude nums[i] (backtrack)
            subset.pop()
            dfs(i + 1)

        dfs(0)
        return result
