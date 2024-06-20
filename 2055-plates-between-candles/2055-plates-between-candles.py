class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        candle_count = 0
        cumulative_candles = []
        for i in range(len(s)):
            if s[i] == "*":
                candle_count += 1
            cumulative_candles.append(candle_count)
      
        
        left_dish = []
        right_dish = []
        left_dish_index = -1
        right_dish_index = -1
        for i in range(len(s)):
            if s[i] == "|":
                left_dish_index = i
            left_dish.append(left_dish_index)
        
        for i in range(len(s)-1, -1, -1):
            if s[i] =="|":
                right_dish_index = i
            right_dish.insert(0,right_dish_index)
            
      
        result = []
        for query in queries:
            
            closest_right_plate = right_dish[query[0]]
            closest_left_plate = left_dish[query[1]]
            
            if closest_right_plate == -1 or closest_left_plate == -1 or closest_right_plate >= closest_left_plate:
                result.append(0)
            else:
                plates_in_between = cumulative_candles[closest_left_plate] - cumulative_candles[closest_right_plate]
                result.append(plates_in_between)
        
        return result
            
            