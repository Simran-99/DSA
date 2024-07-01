class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        hashmap={i:0 for i in arr}
        for i in arr:
            hashmap[i]=hashmap[i]+1
        sorted_hashmap=dict(sorted(hashmap.items(),key=lambda x:x[1],reverse=True))

        n=len(arr)
        count=0
        size=len(arr)
        for i in sorted_hashmap:
            count=count+1
            size=size-sorted_hashmap[i]
            if size<=n/2:
                return count

        return 0
        
