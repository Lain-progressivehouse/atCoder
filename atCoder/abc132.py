from collections import Counter


def p_a():
    s = Counter(input())
    if len(s.keys()) == 2:
        print("Yes")
    else:
        print("No")


def p_b():
    N = int(input())
    p = list(map(int, input().split()))
    ans = 0
    for i in range(N - 2):
        if max(p[i:i + 3]) != p[i + 1] and min(p[i:i + 3]) != p[i + 1]:
            ans += 1

    print(ans)


def p_c():
    N = int(input())
    d = list(map(int, input().split()))

    d.sort()

    print(d[N // 2] - d[N // 2 - 1])


from math import factorial


def cmb(n, r):
    return factorial(n) // factorial(r) // factorial(abs(n - r))


def p_d():
    N, K = map(int, input().split())
    n = N - K + 1
    mod = 10 ** 9 + 7

    for i in range(1, K + 1):
        c = cmb(n, i)
        k = cmb(K - 1, i - 1)
        print(c, k)
        print(c * k % mod)


if __name__ == '__main__':
    p_d()
