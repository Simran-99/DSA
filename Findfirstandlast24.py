class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def find_first(nums,target):
            first_pos=-1
            left,right=0,len(nums)-1
            while left<=right:
                mid=int((left+right)/2)
                if nums[mid]==target:
                    first_pos=mid
                    right=mid-1
                elif nums[mid]>target:
                    right=mid-1
                elif nums[mid]<target:
                    left=mid+1
            return first_pos
        def find_last(nums,target):
            last_pos=-1
            left,right=0,len(nums)-1
            while left<=right:
                mid=int((left+right)/2)
                if nums[mid]==target:
                    last_pos=mid
                    left=mid+1
                elif nums[mid]>target:
                    right=mid-1
                elif nums[mid]<target:
                    left=mid+1
            return last_pos
        
        left_most=find_first(nums,target)
        if left_most==-1:
            return [-1,-1]
        right_most=find_last(nums,target)
        return [left_most,right_most]
        
        
