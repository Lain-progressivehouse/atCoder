"""
A問題: Frog 1
"""


def p_a():
    N = int(input())
    H = list(map(int, input().split()))

    one = []
    two = []
    for i in range(N):
        if i < N - 1:
            one.append(abs(H[i + 1] - H[i]))
        if i < N - 2:
            two.append(abs(H[i + 2] - H[i]))

    ans = []
    ans.append(0)
    ans.append(one[0])

    for i in range(0, N - 2):
        ans.append(min(one[i + 1] + ans[i + 1], two[i] + ans[i]))

    print(ans)


"""
B問題: Frog 2
"""


def p_b():
    N, K = map(int, input().split())
    H = list(map(int, input().split()))
    ans = [10 ** 4 + 1] * N
    ans[0] = 0
    for i in range(1, N):
        k = max(0, i - K)
        for j in range(k, i):
            ans[i] = min(ans[i], ans[j] + abs(H[j] - H[i]))

    print(ans[-1])


"""
c問題: Vacation
"""


def p_c():
    N = int(input())
    before = [0] * 3

    for _ in range(N):
        abc = list(map(int, input().split()))
        for i in range(3):
            abc[i] += max(before[(i + 1) % 3], before[(i + 2) % 3])

        before = abc

    print(max(abc))


"""
D問題: Knapsack 1
"""


def p_d():
    N, W = map(int, input().split())
    dp = [0] * (W + 1)
    for i in range(1, N + 1):
        w, v = map(int, input().split())
        NEXT = [0] * (W + 1)
        for j in range(1, W + 1):
            if j - w >= 0:
                NEXT[j] = max(v + dp[j - w], dp[j])
            else:
                NEXT[j] = dp[j]
        dp = NEXT

    print(max(NEXT))


"""
E問題: Knapsack 2（Wが大きいがvが小さい版）
"""


def p_e():
    N, W = map(int, input().split())
    max_value = 10 ** 3 * N + 1
    dp = [W + 1] * max_value
    dp[0] = 0
    for _ in range(1, N + 1):
        w, v = map(int, input().split())
        NEXT = [W + 1] * max_value
        NEXT[0] = 0
        for i in range(1, max_value):
            if i - v >= 0:
                NEXT[i] = min(dp[i - v] + w, dp[i])
            else:
                NEXT[i] = dp[i]
        dp = NEXT

    ans = 0
    for i, w in enumerate(dp):
        if w <= W:
            ans = i
    print(ans)


"""
F問題: LCS
"""


def p_f():
    S = input()
    T = input()
    s_n = len(S)
    t_n = len(T)
    dp = [[0] * (s_n + 1) for _ in range(t_n + 1)]

    for i in range(1, t_n + 1):
        f = False
        for j in range(1, s_n + 1):
            if S[j - 1] == T[i - 1]:
                f = True
                dp[i][j] = max(dp[i - 1][j - 1] + 1, dp[i - 1][j])
                continue

            if f:
                dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])
            else:
                dp[i][j] = dp[i - 1][j]

    ans = ""
    while s_n > 0 and t_n > 0:
        if dp[t_n - 1][s_n] == dp[t_n][s_n]:
            t_n -= 1

        if dp[t_n][s_n - 1] == dp[t_n][s_n]:
            s_n -= 1

        if dp[t_n - 1][s_n] != dp[t_n][s_n] and dp[t_n][s_n - 1] != dp[t_n][s_n]:
            ans = S[s_n - 1] + ans
            s_n -= 1
            t_n -= 1

    print(ans)


"""
G問題: Longest Path
"""
# メモ化再帰, 再帰回数の上限を上げる必要がある
import sys


def recursion_g(eges, length, f):
    if length[f] != -1:
        return length[f]
    memo = [0]
    for t in eges[f]:
        memo.append(recursion_g(eges, length, t) + 1)
    length[f] = max(memo)
    return length[f]


def p_g():
    sys.setrecursionlimit(10 ** 6)
    N, M = map(int, input().split())
    edges = [[] for _ in range(N)]
    # 各ノードのlengthのメモ
    length = [-1] * N
    for _ in range(M):
        x, y = map(int, input().split())
        edges[x - 1].append(y - 1)

    for i in range(N):
        recursion_g(edges, length, i)
    print(max(length))


# トポロジカルソートしつつDP
from collections import deque


def p_g_dp():
    N, M = map(int, input().split())
    outs = [[] for _ in range(N)]
    ins = [0] * N
    for _ in range(M):
        f, t = map(int, input().split())
        outs[f - 1].append(t - 1)
        ins[t - 1] += 1
    q = deque(t for t in range(N) if ins[t] == 0)
    res = []
    dp = [0] * N
    while q:
        f = q.popleft()
        res.append(f)
        for t in outs[f]:
            ins[t] -= 1
            if ins[t] == 0:
                q.append(t)
                dp[t] = max(dp[t], dp[f] + 1)
    print(max(dp))


"""
H問題: Grid1
"""


def p_h():
    h, w = map(int, input().split())
    dp = []
    for _ in range(h):
        dp.append(list(map(int, input().replace(".", "0 ").replace("#", "-1 ").split())))
    dp[0][0] = 1
    mod = 10 ** 9 + 7

    for i in range(h):
        for j in range(w):
            if j < w - 1 and dp[i][j + 1] != -1 and dp[i][j] != -1:
                dp[i][j + 1] += dp[i][j]
                dp[i][j + 1] %= mod
            if i < h - 1 and dp[i + 1][j] != -1 and dp[i][j] != -1:
                dp[i + 1][j] += dp[i][j]
                dp[i + 1][j] %= mod

    print(dp[-1][-1])


"""
I問題: Coins
"""


def p_i():
    n = int(input())
    *p, = map(float, input().split())
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    dp[0][0] = 1

    for i in range(n):
        for j in range(n):
            dp[i + 1][j + 1] += dp[i][j] * p[i]
            dp[i + 1][j] += dp[i][j] * (1 - p[i])

    print(sum(dp[-1][(n + 1) // 2:]))


"""
J問題: Sushi
"""


def recursion_j(n, dp, i, j, k):
    if dp[i][j][k] > 0:
        return dp[i][j][k]
    if i == j == k == 0:
        return 0.0

    res = 0.0
    if i > 0:
        res += recursion_j(n, dp, i - 1, j, k) * i
    if j > 0:
        res += recursion_j(n, dp, i + 1, j - 1, k) * j
    if k > 0:
        res += recursion_j(n, dp, i, j + 1, k - 1) * k
    res += n
    res *= 1 / (i + j + k)
    dp[i][j][k] = res
    return res


def p_j():
    n = int(input())
    *a, = map(int, input().split())
    c = [0] * 3
    for a_ in a:
        c[a_ - 1] += 1
    dp = [[[0.0] * (n + 1) for _ in range(n + 1)] for _ in range(n + 1)]
    print(recursion_j(n, dp, c[0], c[1], c[2]))


def p_j_dp():
    n = int(input())
    *a, = map(int, input().split())
    c1 = a.count(1)
    c2 = a.count(2)
    c3 = a.count(3)
    dp = [[[0.0] * (n + 1) for _ in range(n + 1)] for _ in range(n + 1)]
    for k in range(c3 + 1):
        for j in range(c3 + c2 + 1 - k):
            for i in range(n + 1 - k - j):
                if i + j + k == 0:
                    continue
                res = n
                if i > 0:
                    res += i * dp[i - 1][j][k]
                if j > 0:
                    res += j * dp[i + 1][j - 1][k]
                if k > 0:
                    res += k * dp[i][j + 1][k - 1]
                res /= i + j + k
                dp[i][j][k] = res
    print(dp[c1][c2][c3])


"""
K問題: Stones
"""


def p_k():
    n, k = map(int, input().split())
    *a, = map(int, input().split())

    dp = [False] * (k + 1)
    for i in range(1, k + 1):
        for j in a:
            if i - j >= 0:
                dp[i] |= not dp[i - j]
    print("First" if dp[k] else "Second")


"""
L問題: Deque
"""


def p_l():
    import sys
    sys.setrecursionlimit(10 ** 6)
    n = int(input())
    *a, = map(int, input().split())
    # dp[i][j]は区間[i,j]が残っているときの最大化
    dp = [[-1] * n for _ in range(n)]

    def dfs(l, r):
        if dp[l][r] != -1:
            return dp[l][r]
        if l == r:
            dp[l][r] = a[l]
            return a[l]
        dp[l][r] = max(a[l] - dfs(l + 1, r), a[r] - dfs(l, r - 1))
        return dp[l][r]

    dfs(0, n - 1)
    print(dp[0][n - 1])


def p_l_2():
    n = int(input())
    *a, = map(int, input().split())
    # dp[i][j]は区間[i,j]が残っているときの最大化
    dp = [[-1] * n for _ in range(n)]

    for i in range(n):
        for l in range(n - i):
            r = l + i
            if l == r:
                dp[l][r] = a[l]
            else:
                dp[l][r] = max(a[l] - dp[l + 1][r], a[r] - dp[l][r - 1])
    print(dp[0][n - 1])


"""
M問題: Candies
"""


def p_m():
    n, k = map(int, input().split())
    *a, = map(int, input().split())
    mod = 10 ** 9 + 7
    # dp[i][j]はi番目の子にj個の飴を配る方法が何通りかどうか
    dp = [[0] * (k + 1) for _ in range(n + 1)]
    for i in range(n + 1):
        dp[i][0] = 1

    for i in range(1, n + 1):
        for j in range(1, k + 1):
            if j - 1 - a[i - 1] >= 0:
                dp[i][j] = (dp[i - 1][j] + dp[i][j - 1] - dp[i - 1][j - 1 - a[i - 1]]) % mod
            else:
                dp[i][j] = (dp[i - 1][j] + dp[i][j - 1]) % mod
    print(dp[n][k])


def p_n():
    from itertools import accumulate
    n = int(input())
    *a, = map(int, input().split())
    ac = list(accumulate(a)) + [0]
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    for i in range(2, n + 1):
        for j in range(n - i + 1):
            print(ac[j + i - 1] - ac[j - 1] + min(dp[k][j] + dp[i - k][j + k] for k in range(1, i)))
            dp[i][j] = ac[j + i - 1] - ac[j - 1] + min(dp[k][j] + dp[i - k][j + k] for k in range(1, i))
    print(dp)
    print(dp[-1][0])


if __name__ == '__main__':
    p_n()
