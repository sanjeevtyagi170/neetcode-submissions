class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_cnt = 0
        cnt = 0
        seen = set(nums)
        for num in nums:
            if num-1 not in seen:
                cnt = 1
                while num+cnt in seen:
                    cnt+=1
                max_cnt = max(max_cnt,cnt)
        return max_cnt
