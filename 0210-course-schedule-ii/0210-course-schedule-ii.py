class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        adj_list = defaultdict(list)
        indegree = defaultdict(int)
        
        for dest, src in prerequisites:
            
            #print(dest, src)
            adj_list[src].append(dest)
    
            # Record each node's in-degree
            indegree[dest] += 1
        
        
        
        print(adj_list,indegree)
        
        q = deque()
        
        for course in range(numCourses):
            if indegree[course] == 0:
                q.append(course)
            
        print(q)        
        res = []
        while q:
            curr = q.popleft()
            print("curr node", curr)
            res.append(curr)
            
            if curr in adj_list:
                for node in adj_list[curr]:

                    indegree[node] -= 1
                    if indegree[node] == 0:
                        q.append(node)
        if len(res) == numCourses:
            return res
        else:
            []

            
        