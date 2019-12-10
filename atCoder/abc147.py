def p_a():
    a = map(int, input().split())
    print("bust" if sum(a) >= 22 else "win")


def p_b():
    s = input()
    length = len(s) // 2
    ans = 0
    for i in range(length):
        if s[i] != s[~i]:
            ans += 1
    print(ans)


def p_c():
    from itertools import combinations
    n = int(input())
    d = [[set() for _ in range(2)] for _ in range(n)]
    for i in range(n):
        a = int(input())
        for _ in range(a):
            x, y = map(int, input().split())
            d[i][y].add(x - 1)
    ans = []
    for i in reversed(range(1, n + 1)):
        for cmb in combinations(range(n), i):
            true_set = set()
            false_set = set()
            for j in range(n):
                if j in cmb:
                    true_set = true_set | d[j][1]
                    false_set = false_set | d[j][0]
                else:
                    false_set.add(j)
            if not true_set & false_set:
                ans.append(n - len(false_set))
    if ans:
        print(max(ans))
    else:
        print(0)


def p_d():
    n = int(input())
    *A, = map(int, input().split())
    mod = 10 ** 9 + 7
    max_bit = len(bin(max(A))) - 2
    ans = 0
    for i in range(max_bit):
        count = [0] * 2
        for a in A:
            count[a >> i & 1] += 1
        ans += (1 << i) * count[0] * count[1]
        ans %= mod
    print(ans)


"""
bool値でDPするならbitの1,0をtrue,falseで判定すれば纏めて処理ができて早い
"""


def p_e():
    from itertools import product
    h, w = map(int, input().split())
    t1 = [list(map(int, input().split())) for _ in range(h)]
    t2 = [list(map(int, input().split())) for _ in range(h)]

    # pythonでbitsetを用いる->boolのDPで2進数の1をTrue, 0をFalseとして扱う
    # 右にxシフト = その値にx足した値    (10001)<<4 -> (100010000)
    m = 160 * 80
    dp = [[0] * w for _ in range(h)]
    dp[0][0] = 1 << m
    for i, j in product(range(h), range(w)):
        v = abs(t1[i][j] - t2[i][j])
        if i > 0:
            dp[i][j] |= dp[i - 1][j]
        if j > 0:
            dp[i][j] |= dp[i][j - 1]
        dp[i][j] = (dp[i][j] << v) | (dp[i][j] >> v)

    ans = m
    for i in range(m * 2):
        if dp[h - 1][w - 1] & (1 << i) > 0:
            ans = min(ans, abs(m - i))
    print(ans)


def p_f():
    n, x, d = map(int, input().split())
    ans = 1 << n
    print(ans)


if __name__ == '__main__':
    p_e()
