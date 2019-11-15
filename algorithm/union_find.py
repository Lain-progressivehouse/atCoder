"""
union-find木
"""


class UnionFind:
    def __init__(self, n):
        self.par = list(range(n))
        self.rank = [0] * n
        self.size = [1] * n

    def find(self, x):
        if self.par[x] == x:
            return x
        self.par[x] = self.find(self.par[x])
        return self.par[x]

    def unite(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
        if self.rank[x] < self.rank[y]:
            self.par[x] = y
            x, y = y, x
        else:
            self.par[y] = x
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1
        self.size[x] += self.size[y]

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def get_size(self, x):
        return self.size[self.find(x)]


def abc075_c():
    n, m = map(int, input().split())
    ab = [tuple(map(int, input().split())) for _ in range(m)]

    ans = 0
    for i in range(m):
        uf = UnionFind(n)
        for j in range(m):
            if i == j:
                continue
            uf.unite(ab[j][0] - 1, ab[j][1] - 1)

        print(uf.rank)
        s = set()
        for j in range(n):
            s.add(uf.find(j))
        if len(s) > 1:
            ans += 1

    print(ans)


def abc120_d():
    n, m = map(int, input().split())
    ab = [map(lambda x: int(x) - 1, input().split()) for _ in range(m)]

    ans = n * (n - 1) // 2
    uf = UnionFind(n)
    res = []
    for a, b in reversed(ab):
        res.append(ans)
        if not uf.same(a, b):
            ans -= uf.get_size(a) * uf.get_size(b)
        uf.unite(a, b)
    print("\n".join(map(str, reversed(res))))


from collections import Counter


def abc049_d():
    n, k, l = map(int, input().split())

    road = UnionFind(n)
    for i in range(k):
        p, q = map(int, input().split())
        road.unite(p - 1, q - 1)

    rail = UnionFind(n)
    for i in range(l):
        r, s = map(int, input().split())
        rail.unite(r - 1, s - 1)

    set1 = []
    for i in range(n):
        set1.append((road.find(i), rail.find(i)))
    c = Counter(set1)
    ans = []
    for i in range(n):
        ans.append(c[(road.find(i), rail.find(i))])
    print(*ans)


if __name__ == '__main__':
    # abc075_c()
    # abc120_d()
    abc049_d()
