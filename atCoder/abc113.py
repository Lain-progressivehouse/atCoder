def p_a():
    x, y = map(int, input().split())
    print(x + y // 2)


def p_b():
    n = int(input())
    t, a = map(int, input().split())
    *H, = map(int, input().split())
    ans = 10 ** 9
    idx = -1
    for i, h in enumerate(H):
        if ans > abs(a - (t - h * 0.006)):
            ans = abs(a - (t - h * 0.006))
            idx = i + 1
    print(idx)


def p_c():
    from collections import defaultdict
    from bisect import bisect
    n, m = map(int, input().split())
    py = [tuple(map(int, input().split())) for _ in range(m)]
    d = defaultdict(list)
    for p, y in py:
        d[p].append(y)
    for key in d.keys():
        d[key].sort()
    for p, y in py:
        print("{:06}{:06}".format(p, bisect(d[p], y)))


def p_d():
    """
    あみだくじ
    動的計画法で解く。wからwに行く遷移はフィボナッチ数列から求まる
    :return:
    """
    H, W, K = map(int, input().split())
    mod = 10 ** 9 + 7
    dp = [0] * W
    dp[0] = 1
    fib = [1, 1]
    for i in range(2, W):
        fib.append(fib[i - 2] + fib[i - 1])
    some = [0] * W
    for i in range(W):
        some[i] = fib[i] * fib[W - i - 1]
    some_2 = [0] * (W - 1)
    for i in range(W - 1):
        some_2[i] = fib[i] * fib[W - i - 2]
    for i in range(1, H + 1):
        w = 0
        NEXT = [0] * W
        for j in range(W):
            if j > 0:
                NEXT[j - 1] += dp[j] * some_2[j - 1]
                NEXT[j - 1] %= mod
            if j < W - 1:
                NEXT[j + 1] += dp[j] * some_2[j]
                NEXT[j + 1] %= mod
            if dp[j] > 0:
                NEXT[j] += dp[j] * some[j]
                NEXT[j] %= mod
            w += 1
        dp = NEXT
    print(dp[K - 1] % mod)


if __name__ == '__main__':
    p_d()
