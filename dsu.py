# Based on the implementation described here -> https://e-maxx.ru/algo/dsu

class DSU:
    """Disjoint set union."""
    
    def __init__(self, n=0):
        """Create a dsu of size n (zero by default)."""
        self.dsu = list(range(n))
        self.rank = [0] * n
    
    def __len__(self):
        return len(self.dsu)
    
    def __repr__(self):
        return repr(self.dsu)
    
    def __str__(self):
        return repr(self.get_sets())
    
    def __getitem__(self, i):
        return self.dsu[i]
    
    def __setitem__(self, k, v):
        self.dsu[k] = v
    
    def make_sets(self, q=1):
        """Add q new sets."""
        n = len(self)
        self.dsu.extend(range(n, n+q))
        self.rank.extend([0] * q)
    
    def find_set(self, x: int) -> int:
        """Find the leader of the set to which x belongs."""
        if self[x] == self[self[x]]:
            return self[x]
        self[x] = self.find_set(self[x])  # Path compression heuristic
        return self[x]
    
    def union_sets(self, x: int, y: int):
        """Join sets to which x and y belong."""
        try:
            x = self.find_set(x)
            y = self.find_set(y)
            if x != y:
                # Rank heuristic (based on tree depth)
                if self.rank[x] < self.rank[y]:
                    x,y = y,x
                self[y] = x
                if self.rank[x] == self.rank[y]:
                    self.rank[x] += 1
            self[x] = self[y]
        except IndexError:
            print('At least one of the sets does not exist.')
    
    def compress(self):
        """Compress all paths."""
        for x,_ in enumerate(self.dsu):
            self.find_set(i)
    
    def get_sets(self):
        """Get {leader: elements} dictionary."""
        rng = range(len(self))
        sets = {k: set() for k in {self.find_set(x) for x in rng}}
        for x in rng:
            sets[self.find_set(x)].add(x)
        return sets
