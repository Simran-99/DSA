class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        ans=[]
        s=set()
        for i in range(0, len(nums)):
            for j in range(i+1,len(nums)):
                k=j+1
                l=len(nums)-1
                while k<l:
                    calculated_sum=nums[i]+nums[j]+nums[k]+nums[l]
                    if calculated_sum==target:
                        temp_list=[nums[i],nums[j],nums[k],nums[l]]
                        s.add(tuple(temp_list))
                        k=k+1
                        l=l-1
                    elif calculated_sum<target:
                        k=k+1
                    elif calculated_sum>target:
                        l=l-1
        ans=list(s)
        return ans
                
        
