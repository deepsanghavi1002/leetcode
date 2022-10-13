class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        i = 1
        tempString = a
        while(True):
            tempString = i * a
            if len(tempString) >10000:
                break
            if b in tempString:
                
                return i
            
            
            #print(tempString, i)
            i += 1
        print(len(tempString))
        return - 1