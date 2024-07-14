class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hashmap1=defaultdict(int)
        hashmap2=defaultdict(int)
        lst_array=[]
        for i in nums1:
            hashmap1[i]=hashmap1[i]+1
        for j in nums2:
            hashmap2[j]=hashmap2[j]+1
        
        for i in hashmap1:
            if i in hashmap2:
                lst_array.append(i)
        
        return lst_array
            
