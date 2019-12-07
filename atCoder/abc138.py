def p_a():
    a = int(input())
    s = input()
    if a >= 3200:
        print(s)
    else:
        print("red")


def p_b():
    N = int(input())
    A = list(map(int, input().split()))

    a = 0
    for i in A:
        a += 1 / i

    print(1 / a)


def p_c():
    N = int(input())
    V = list(map(int, input().split()))
    ans = 0

    for _ in range(N - 1):
        V.sort()
        ans = (V.pop(0) + V.pop(0)) / 2
        V.append(ans)

    print(ans)


from collections import defaultdict


def p_d():
    N, Q = map(int, input().split())
    l = defaultdict(list)
    ans = [0] * N

    for _ in range(N - 1):
        a, b = map(int, input().split())
        l[a].append(b)

    for _ in range(Q):
        p, x = map(int, input().split())
        ans[p - 1] += x

    for i in range(N):
        for j in l[i]:
            ans[j - 1] += ans[i - 1]

    print(*ans)


from bisect import *


def p_e():
    s = input()
    t = input()
    l = defaultdict(list)

    for i, c in enumerate(list(s)):
        l[c].append(i + 1)

    for c in list(t):
        if c not in l.keys():
            print(-1)
            exit()

    N = 0
    current = -1
    for c in list(t):
        R = l[c]

        x = bisect(R, current)

        if len(R) == x:
            N += 1
            current = R[0]
        else:
            current = R[x]

    print(N * len(s) + current)


def p_f():
    L, R = map(int, input().split())
    mod = 10 ** 9 + 7
    # dp[i][j][k][l]: iは桁, jはL<=xか, kはy<=Rか, lは桁数が同じか
    dp = [[[[0] * 2 for _ in range(2)] for _ in range(2)] for _ in range(61)]
    dp[60][0][0][0] = 1
    for i in reversed(range(60)):
        # LとRのiビット目を取り出す
        lb = L >> i & 1
        rb = R >> i & 1
        for j in range(2):
            for k in range(2):
                for l in range(2):
                    # 前の状態
                    pre = dp[i + 1][j][k][l]
                    for x in range(2):
                        for y in range(2):
                            nj, nk, nl = j, k, l
                            if x and (not y):  # xが1でyが0
                                continue
                            if (not l) and x != y:
                                continue
                            if x and y:
                                nl = 1
                            # j: L <= x
                            if (not j) and (not x) and lb:
                                continue
                            if x and (not lb):
                                nj = 1
                            # k: y <= R
                            if (not k) and y and (not rb):
                                continue
                            if (not y) and rb:
                                nk = 1
                            dp[i][nj][nk][nl] += pre

    ans = 0
    for j in range(2):
        for k in range(2):
            for l in range(2):
                ans += dp[0][j][k][l]
                ans %= mod
    print(ans)

if __name__ == '__main__':
    p_f()
