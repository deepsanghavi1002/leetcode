class UnionFind:
    def __init__(self, size):
        self.root = [i for i in range(size)]
        self.rank = [1]*size
        
    def find(self, x):
        if self.root[x] != x:
            return self.find(self.root[x])
        return self.root[x]
    
    def union(self, x, y):
        
        rootX = self.find(x)
        rootY = self.find(y)
        
      

        if self.rank[rootX] > self.rank[rootY]:
            self.root[rootY] = rootX
        elif self.rank[rootX] < self.rank[rootY]:
            self.root[rootX] = rootY

        else:
            self.root[rootY] = rootX
            self.rank[rootX] += 1
            
    def connected(self, x,y):
        return self.find(x) == self.find(y)

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:

        
        weights = []
        
        for node1 in range(len(points)):
            for node2 in range(node1+1,len(points)):
            
       
                dist = abs(points[node1][0] - points[node2][0]) + abs(points[node1][1] - points[node2][1])
                weights.append([dist, node1, node2])
                
        weights = sorted(weights, key = lambda x:x[0])
        
   
   
        
        
        uf = UnionFind(len(points))
        edges = len(points) - 1
        cost = 0
        
        for weight, node1, node2 in weights:
            if not uf.connected(node1,node2):
                uf.union(node1,node2)
                cost+=weight
                edges -=1
            if edges == 0:
                return cost
        
        
        return cost