from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()          
        n = len(nums)
        res = []

        for i in range(n - 2):
            x = nums[i]
            if x + nums[i + 1] + nums[i + 2] > 0:
                break
            if x + nums[n - 2] + nums[n - 1] < 0:
                continue
            if i > 0 and x == nums[i - 1]:
                continue

            left, right = i + 1, n - 1
            target = -x
            while left < right:
                s = nums[left] + nums[right]
                if s < target:
                    left += 1
                elif s > target:
                    right -= 1
                else:
                    res.append([x, nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

        return res