class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        max_w=0
        l=0
        r=0
        max_zeros=0
        for r in range(len(nums)):
            if nums[r]==0:
                max_zeros=max_zeros+1
            while max_zeros>k:
                if nums[l]==0:
                    max_zeros=max_zeros-1
                l=l+1
            w=r-l+1
            max_w=max(max_w,w)
        return max_w
            

        
