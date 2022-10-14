# class Solution:
#     def repeatedStringMatch(self, a: str, b: str) -> int:
#         i = 1
#         tempString = a
#         while(True):
#             tempString = i * a
#             if len(tempString) >10000:
#                 break
#             if b in tempString:
                
#                 return i
            
            
#             #print(tempString, i)
#             i += 1
#         print(len(tempString))
#         return - 1
class Solution(object):
    def repeatedStringMatch(self, A, B):
        times = -(-len(B) // len(A)) # Equal to ceil(len(b) / len(a))
        for i in range(2):
          if B in (A * (times + i)):
            return times + i
        return -1
