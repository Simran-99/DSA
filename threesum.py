from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        final_ans = []
        
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            start, end = i + 1, len(nums) - 1
            while start < end:
                ans = nums[i] + nums[start] + nums[end]
                if ans == 0:
                    final_ans.append([nums[i], nums[start], nums[end]])
                    start += 1
                    end -= 1
                    while start < end and nums[start] == nums[start - 1]:
                        start += 1
                    while start < end and nums[end] == nums[end + 1]:
                        end -= 1
                elif ans < 0:
                    start += 1
                else:
                    end -= 1
        return final_ans
