class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        temp = {}
        for i in range(len(nums)):
            temp[nums[i]] = i
        
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in temp and temp[complement] != i:
                return [i, temp[complement]]
        