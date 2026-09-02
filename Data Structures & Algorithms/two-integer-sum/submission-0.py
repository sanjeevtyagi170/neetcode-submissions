class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = {}
        for i in range(len(nums)):
            saver = target - nums[i]
            if saver in hash:
                return [hash[saver], i]
            else:
                hash[nums[i]]=i
