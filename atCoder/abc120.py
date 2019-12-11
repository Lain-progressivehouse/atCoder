def p_a():
    a, b, c = map(int, input().split())
    print(min(b // a, c))


def p_b():
    a, b, k = map(int, input().split())
    count = 0
    for i in reversed(range(min(a, b) + 1)):
        if a % i == b % i == 0:
            count += 1
        if count == k:
            print(i)
            break


def p_c():
    s = input()
    a = s.count("0")
    b = s.count("1")
    print(min(a, b) * 2)


def p_d():
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


if __name__ == '__main__':
    p_d()
