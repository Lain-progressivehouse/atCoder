def p_a():
    y, m, d = map(int, input().split("/"))
    ans = "Heisei"
    if y == 2019:
        if m > 4:
            ans = "TBD"
    elif y > 2019:
        ans = "TBD"
    print(ans)


def p_b():
    n = int(input())
    ans = 0
    for _ in range(n):
        x, u = input().split()
        x = float(x)
        if u == "BTC":
            x *= 380000.0
        ans += x
    print(ans)


def p_c():
    """
    全探索で
    :return:
    """
    n, A, B, C = map(int, input().split())
    li = [int(input()) for _ in range(n)]
    INF = 10 ** 9

    def dfs(cur, a, b, c):
        if cur == n:
            return abs(A - a) + abs(B - b) + abs(C - c) - 30 if min(a, b, c) > 0 else INF
        ret1 = dfs(cur + 1, a, b, c)
        ret2 = dfs(cur + 1, a + li[cur], b, c) + 10
        ret3 = dfs(cur + 1, a, b + li[cur], c) + 10
        ret4 = dfs(cur + 1, a, b, c + li[cur]) + 10
        return min(ret1, ret2, ret3, ret4)

    print(dfs(0, 0, 0, 0))


def p_d():
    from bisect import bisect_right
    A, B, Q = map(int, input().split())
    INF = 10 ** 18
    s = [-INF] + [int(input()) for _ in range(A)] + [INF]
    t = [-INF] + [int(input()) for _ in range(B)] + [INF]
    ans = []
    for _ in range(Q):
        x = int(input())
        b, d = bisect_right(s, x), bisect_right(t, x)
        res = INF
        for S in [s[b - 1], s[b]]:
            for T in [t[d - 1], t[d]]:
                d1, d2 = abs(S - x) + abs(T - S), abs(T - x) + abs(S - T)
                res = min((d1, d2, res))
        ans.append(str(res))
    print("\n".join(ans))


if __name__ == '__main__':
    p_d()
