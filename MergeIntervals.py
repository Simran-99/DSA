class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda i:i[0])
        output=[]
        start=intervals[0][0]
        end=intervals[0][1]
        for i in range(1,len(intervals)):
            if intervals[i][0]>=start and intervals[i][0]<=end:
                end=max(intervals[i][1],end)
            else:
                output.append([start,end])
                start=intervals[i][0]
                end=intervals[i][1]
        if [start,end] not in output:
            output.append([start,end])
        return output
