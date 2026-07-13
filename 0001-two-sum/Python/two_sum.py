class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # First pass: store all numbers in hashmap
        hashmap = {}
        for i in range(len(nums)):
            hashmap[nums[i]] = i
            
        # Second pass: check for complements
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashmap and hashmap[complement] != i:
                return [i, hashmap[complement]]
                
        # In case there is no solution
        return None