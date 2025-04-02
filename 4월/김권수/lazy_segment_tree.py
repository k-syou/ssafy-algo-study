class LazySeg:
    def __init__(self, N):
        self.n = N
        size = 1
        while size < N:
            size *= 2
        self.tree = [0] * (size * 2)
        self.lazy = [0] * (size * 2)

    def _propagate(self, start, end, node):
        if self.lazy[node] != 0:
            self.tree[node] += self.lazy[node] 
            if start != end:
                self.lazy[node * 2] += self.lazy[node] 
                self.lazy[node * 2 + 1] += self.lazy[node] 
            self.lazy[node] = 0


    def _update(self, node, l, r, start, end, v):
        # print(node, l, r, start, end)
        if end < l  or start > r:
            return
        self._propagate(start, end, node)
        if l <= start and end <= r:
            self.tree[node] += v
            if start != end:
                self.lazy[node * 2] += v
                self.lazy[node * 2 + 1] += v
            return
        mid = (start + end) // 2
        self._update(node * 2, l, r, start, mid, v)
        self._update(node * 2 + 1, l, r, mid + 1, end, v)

    def add(self, l, r):
        self._update(1, l, r, 0, self.n, 1)
    

    def remove(self, l, r):
        self._update(1, l, r, 0, self.n, -1)


    def _query(self, start, end, x, node):
        if end < x or start > x:
            return 0
        self._propagate(start, end, node)
        if end == start:
            return self.tree[node]
        mid = (start + end) // 2
        if x <= mid:
            return self._query(start, mid, x, node * 2)
        else:
            return self._query(mid + 1, end, x, node * 2 + 1)

    def query(self, x):
        return self._query(0, self.n, x, 1)

if __name__ == '__main__':
    N = 2000000
    seg = LazySeg(N)
    seg.add(0, 10000 - 100)
    seg.add(2001, 10000 - 100)
    seg.add(0, 2099 - 100)
    seg.remove(0, 10000 - 100)
    print(seg.query(2000))