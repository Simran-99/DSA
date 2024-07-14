class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        hashmap_fruits=defaultdict(int)
        l=0
        total=0
        res=0
        for i in fruits:
            hashmap_fruits[i]=hashmap_fruits[i]+1
            total=total+1

            while len(hashmap_fruits)>2:
                f=fruits[l]
                hashmap_fruits[f]=hashmap_fruits[f]-1
                total=total-1
                l=l+1
                if not hashmap_fruits[f]:
                    hashmap_fruits.pop(f)
            res=max(res,total)
        return res
        
