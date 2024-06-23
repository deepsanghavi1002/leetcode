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
        if rootX == rootY:
            
            return False
        else:
            
            if self.rank[rootX] > self.rank[rootY]:
                self.root[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.root[rootX] = rootY

            else:
                self.root[rootY] = rootX
                self.rank[rootX] += 1
            return True
    def connected(self, x,y):
        return self.find(x) == self.find(y)
    
class Solution:
    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
        lastUnionTime = 0
        comp = n
        uf = UnionFind(n)
        logs = sorted(logs, key =  lambda x:x[0])
        print(logs)
        for time,x,y in logs:
            if uf.union(x,y) == True:
                comp -= 1
                lastUnionTime = time
        
        if comp != 1:
            return -1
        return lastUnionTime