class UnionFind:
    def __init__(self, size):
        self.root = [i for i in range(size)]
        self.rank = [1]*size
    def find(self, x):
        if self.root[x] != x:
            self.root[x] = self.find(self.root[x])  # Path compression
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
            self.rank[rootX] += self.rank[rootY]
           
    def connected(self, x,y):
        return self.find(x) == self.find(y)
    
    
class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        n = len(s)
        componensts = n 
        
        uf = UnionFind(n)
        
        for x,y in pairs:
            uf.union(x,y)
        
        d = defaultdict(list)
        for i in range(n):
            d[uf.find(i)].append(s[i])
        
        for key, value in d.items():
            value.sort()
        res = ""
        for i in range(n):
            res += d[uf.find(i)].pop(0)
            
        return res