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


def p_e():
    h, w = map(int, input().split())
    t = [list(map(int, input().split())) for _ in range(h)]
    m = 0
    for i in range(h):
        *b, = map(int, input().split())
        for j, e in enumerate(b):
            t[i][j] = abs(t[i][j] - e)
            if m < abs(t[i][j] - e):
                m = abs(t[i][j] - e)

    # dp[i][j][k]: (i,j)でkになるかどうかbool値
    bool_width = m * (h + w)
    dp = [[[False] * bool_width for _ in range(w)] for _ in range(h)]
    for i in range(h):
        for j in range(w):
            if i == j == 0:
                dp[i][j][t[i][j]] = True
                continue
            for k in range(bool_width):
                if i > 0:
                    if abs(k + t[i][j]) < bool_width:
                        dp[i][j][k] |= dp[i - 1][j][abs(k + t[i][j])]
                    if abs(k - t[i][j]) < bool_width:
                        dp[i][j][k] |= dp[i - 1][j][abs(k - t[i][j])]
                if j > 0:
                    if abs(k + t[i][j]) < bool_width:
                        dp[i][j][k] |= dp[i][j - 1][abs(k + t[i][j])]
                    if abs(k - t[i][j]) < bool_width:
                        dp[i][j][k] |= dp[i][j - 1][abs(k - t[i][j])]
    for i, e in enumerate(dp[-1][-1]):
        if e:
            print(i)
            break


def p_f():
    n, x, d = map(int, input().split())
    ans = 1 << n
    print(ans)


if __name__ == '__main__':
    p_e()
