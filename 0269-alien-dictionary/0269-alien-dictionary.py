class Solution:
    def alienOrder(self, words: List[str]) -> str:
        adj = defaultdict(set)
        indegree = Counter({c : 0 for word in words for c in word})
        
        for first, second in zip(words, words[1:]):
            for c,d in zip(first, second):
                if c != d:
                    if d not in adj[c]:
                        adj[c].add(d)
                        indegree[d] += 1
                    break
            else:
                if len(second) < len(first): 
                    return ""
                    
            
            
          
                
          
                
        
        q = deque()
        
        for elem in indegree:
            if indegree[elem] == 0 :
                q.append(elem)
   
        
        res = []
        
        while q:
            curr = q.popleft()
            res += curr
            for elem in adj[curr]:
                 
                indegree[elem] -= 1
                
                if indegree[elem] == 0:
                    q.append(elem)
                   
                
        if len(res) < len(indegree):
            return ""
        return "".join(res)
            