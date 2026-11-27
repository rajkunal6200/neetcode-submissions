from typing import List

class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        path = []

        def dfs(i, total):
            if total == target:
                result.append(path.copy())
                return  # Must be indented inside the if-block

            if i == len(nums) or total > target:
                return

            # Decision 1: Include nums[i] (stay at index i to allow reuse)
            path.append(nums[i])
            dfs(i, total + nums[i])

            # Decision 2: Exclude nums[i] (move to index i + 1)
            path.pop()
            dfs(i + 1, total)

        dfs(0, 0)
        return result
