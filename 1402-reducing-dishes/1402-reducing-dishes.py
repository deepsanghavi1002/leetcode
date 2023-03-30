class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort(reverse = True)
        n = len(satisfaction)
        presum = 0
        res = 0

        for i in range(n):
            print(satisfaction, i)
            presum += satisfaction[i]
            print(presum)
            print("===")
            if presum < 0:
                break
            
            res+= presum
            print(res)
        return res
