class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        tuples = defaultdict(list)
     
        for (time, site, user) in sorted(zip(timestamp, website, username)):
            tuples[user].append(site)
            
            
        score = defaultdict(int)
        for user, website in tuples.items():
            for pattern in set(combinations(website, 3)):
                score[pattern] += 1
                
                
        print(score)
        max_score = 0
        max_pattern = ''
        for pattern, score in score.items():
            if score > max_score or (score == max_score and pattern < max_pattern):
                max_pattern = pattern 
                max_score = score
            
        print(max_score, max_pattern)
        return max_pattern
        
        
        
        