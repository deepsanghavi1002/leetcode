class Solution:
    def reorganizeString(self, s: str) -> str:
        
        pq = [(-count, char) for char, count in Counter(s).items()]
        heapify(pq)
        res = ""
        
        while len(pq)>1:
            
            count1, char1 = heappop(pq)
            count2, char2 = heappop(pq)
            
            
            res+= char1 + char2
            


            if count1 != -1 :
                heappush(pq, (count1 + 1, char1))
            if count2 != -1:
                heappush(pq, (count2 +1, char2))
            #print(res, pq)
        if pq:
            count,char = heappop(pq)
            if count != -1:
                return ""
            else:
                res += char
        return res
                            
            
