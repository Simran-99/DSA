class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num_str=""
        lst=[]
        for i in digits:
            num_str=num_str+str(i)
        num=int(num_str)
        num=num+1
        final_num_str=str(num)
        for i in range(len(final_num_str)):
            lst.append(int(final_num_str[i]))
        return lst

        
