def p_a():
    d = {"A": "T", "T": "A", "C": "G", "G": "C"}
    print(d[input()])


def p_b():
    s = input()
    s = s.replace("A", ".").replace("T", ".").replace("C", ".").replace("G", ".")
    ans = 0
    tmp = 0
    for e in s:
        if e != ".":
            ans = max(ans, tmp)
            tmp = 0
        else:
            tmp += 1
    ans = max(ans, tmp)
    print(ans)


class SegmentTree:
    def __init__(self, n, init_val, ide_ele=0):
        self.num = 2 ** (n - 1).bit_length()
        self.seg = [ide_ele] * 2 * self.num
        self.ide_ele = ide_ele
        for i in range(n):
            self.seg[i + self.num - 1] = init_val[i]
        for i in range(self.num - 2, -1, -1):
            self.seg[i] = self.seg_func(self.seg[2 * i + 1], self.seg[2 * i + 2])

    def update(self, k, x):
        k += self.num - 1
        self.seg[k] = x
        while k:
            k = (k - 1) // 2
            self.seg[k] = self.seg_func(self.seg[2 * k + 1], self.seg[2 * k + 2])

    def query(self, p, q):
        if q <= p:
            return self.ide_ele
        p += self.num - 1
        q += self.num - 2
        res = self.ide_ele
        while q - p > 1:
            if p & 1 == 0:
                res = self.seg_func(res, self.seg[p])
            if q & 1 == 1:
                res = self.seg_func(res, self.seg[q])
                q -= 1
            p = p // 2
            q = (q - 1) // 2
        if p == q:
            res = self.seg_func(res, self.seg[p])
        else:
            res = self.seg_func(self.seg_func(res, self.seg[p]), self.seg[q])
        return res

    def seg_func(self, x, y):
        return x + y


def p_c():
    n, q = map(int, input().split())
    s = input().replace("AC", "01")
    li = list(map(lambda x: 1 if x == "0" else 0, s))
    seg = SegmentTree(n, li)
    ans = []
    for _ in range(q):
        l, r = map(int, input().split())
        ans.append(str(seg.query(l - 1, r - 1)))
    print("\n".join(ans))


def p_d():
    n = int(input())
    mod = 10 ** 9 + 7
    # dp[i][j][k][l]: 長さiの文字列でi-2番目がj、i-1番目がk、i番目がlであるものの総数
    dp = [[[[0] * 4 for _ in range(4)] for _ in range(4)] for _ in range(n + 1)]
    for j in range(4):
        for k in range(4):
            for l in range(4):
                if j == 1 and k == 2 and l == 3:
                    continue
                if j == 2 and k == 1 and l == 3:
                    continue
                if j == 1 and k == 3 and l == 2:
                    continue
                dp[3][j][k][l] = 1
    for i in range(4, n + 1):
        for j in range(4):
            for k in range(4):
                for l in range(4):
                    for m in range(4):
                        if j == 1 and k == 2 and l == 3:
                            continue
                        if j == 2 and k == 1 and l == 3:
                            continue
                        if j == 1 and k == 3 and l == 2:
                            continue
                        if m == 1 and k == 2 and l == 3:
                            continue
                        if m == 1 and j == 2 and l == 3:
                            continue
                        dp[i][j][k][l] += dp[i - 1][m][j][k]
                        dp[i][j][k][l] %= mod

    ans = 0
    for j in range(4):
        for k in range(4):
            for l in range(4):
                ans += dp[n][j][k][l]
                ans %= mod
    print(ans)


if __name__ == '__main__':
    p_d()
