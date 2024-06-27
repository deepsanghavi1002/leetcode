class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        start = [i[0] for i in intervals]
        end = [i[1] for i in intervals]
        
        
        
        last = max(end) 
        
        dp =[0]*(last +1)
        
        for i in range(len(start)):
            dp[start[i]] += 1
            dp[end[i]] -= 1
        print(dp)   
        rooms = 0
        res = 0
        for i in dp:
            rooms += i
            
            res = max(res,rooms)
        return res