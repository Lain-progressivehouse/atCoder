def p_a():
    print(int(input()) ** 2)


def p_b():
    n = int(input())
    s = input()
    if n & 1 == 1:
        print("No")
    else:
        if s[:n // 2] == s[n // 2:]:
            print("Yes")
        else:
            print("No")


def p_c():
    from itertools import permutations
    from math import sqrt
    n = int(input())
    xy = [tuple(map(int, input().split())) for _ in range(n)]
    ans = []
    for per in permutations(list(range(n))):
        x, y = xy[per[0]]
        dist = 0
        for i in per[1:]:
            x2, y2 = xy[i]
            dist += sqrt((x2 - x) ** 2 + (y2 - y) ** 2)
            x, y = x2, y2
        ans.append(dist)
    print(sum(ans) / len(ans))


def p_d():
    x, y = map(int, input().split())
    if y > x:
        x, y = y, x
    if (x + y) % 3 != 0:
        print(0)
        exit()
    if x - y > (x + y) // 3:
        print(0)
        exit()
    x, y = x - (x + y) // 3, y - (x + y) // 3

    def c_mod(n, r, mod=10 ** 9 + 7):
        n1, r = n + 1, min(r, n - r)
        num = den = 1
        for i in range(1, r + 1):
            num = num * (n1 - i) % mod
            den = den * i % mod
        return num * pow(den, mod - 2, mod) % mod

    print(c_mod(x + y, y))


def p_e():
    n, t = map(int, input().split())
    ab = [tuple(map(int, input().split())) for _ in range(n)]
    ab.sort()
    ma = ab[-1][0]
    dp = [0] * (t + ma)
    for w, v in ab:
        next = [0] * (t + ma)
        for j in range(1, t + ma):
            if 0 <= j - w < t:
                next[j] = max(dp[j - w] + v, dp[j])
            else:
                next[j] = dp[j]
        dp = next
    print(max(dp))


def p_f():
    pass


if __name__ == '__main__':
    p_e()
