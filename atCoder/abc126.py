def p_a():
    n, k = map(int, input().split())
    s = input()
    print(s[:k - 1] + str.lower(s[k - 1]) + s[k:])


def p_b():
    s = input()
    if 1 <= int(s[0:2]) < 13:
        if 1 <= int(s[2:4]) < 13:
            print("AMBIGUOUS")
        else:
            print("MMYY")
    else:
        if 1 <= int(s[2:4]) < 13:
            print("YYMM")
        else:
            print("NA")


def p_c():
    n, k = map(int, input().split())
    ans = 0
    m = min(n, k - 1)
    for i in range(1, m + 1):
        x = 0
        while k > i << x:
            x += 1
        ans += (1 / n) * (1 / (1 << x))
    if m == k - 1:
        ans += (n - k + 1) / n

    print(ans)


def p_d():
    from sys import stdin
    input = stdin.readline
    import sys
    sys.setrecursionlimit(10 ** 6)
    n = int(input())
    route = [[] for _ in range(n)]
    for _ in range(n - 1):
        u, v, w = map(int, input().split())
        w = 0 if w & 1 == 0 else 1
        route[u - 1].append((v - 1, w))
        route[v - 1].append((u - 1, w))

    ans = [-1] * n

    def dfs(p, d):
        ans[p] = d
        for i, j in route[p]:
            if ans[i] < 0:
                dfs(i, d ^ j)

    dfs(0, 0)
    print("\n".join(map(str, ans)))


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


def p_e():
    n, m = map(int, input().split())
    uf = UnionFind(n)
    for _ in range(m):
        x, y, z = map(int, input().split())
        uf.unite(x - 1, y - 1)
    ans = set()
    for i in range(n):
        ans.add(uf.find(i))
    print(len(ans))


from collections import deque


def p_f():
    m, k = map(int, input().split())
    length = 1 << (m + 1)
    n = 1 << m
    if n <= k:
        print(-1)
        exit()

    if m == 1 and k == 0:
        print("0 0 1 1")
        exit()
    elif m == 1 and k == 1:
        print(-1)
        exit()

    d = deque()
    d.append(k)
    for i in range(n):
        if i == k:
            continue
        d.append(i)
        d.appendleft(i)
    d.append(k)
    print(*d)


if __name__ == '__main__':
    p_f()
