class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], i]
            seen[num] = i
        return []
    
# Leetcode Two Sum problem: https://leetcode.com/problems/two-sum/  

# Example usage:
solution = Solution()
print(solution.twoSum([2, 7, 11, 15], 9))