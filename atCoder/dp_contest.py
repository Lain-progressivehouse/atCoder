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


if __name__ == '__main__':
    p_f()
