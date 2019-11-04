def p_a():
    a, b = map(int, input().split())
    print(max(a - b * 2, 0))


def p_b():
    N = int(input())
    d = list(map(int, input().split()))
    ans = 0
    for i in range(N - 1):
        for j in range(i + 1, N):
            ans += d[i] * d[j]

    print(ans)


def p_c():
    n = int(input())
    S = input()
    bf = ""
    ans = 0
    for s in S:
        if bf != s:
            ans += 1
        bf = s
    print(ans)


from bisect import bisect_left


def p_d():
    N = int(input())
    L = list(map(int, input().split()))
    L.sort()
    ans = N * (N - 1) * (N - 2) // 6

    for i in range(N - 2):
        for j in range(i + 1, N - 1):
            b = bisect_left(L, L[i] + L[j])
            if b != N:
                ans -= N - b

    print(ans)


def p_e():
    pass


def p_f():
    pass


if __name__ == '__main__':
    p_a()
