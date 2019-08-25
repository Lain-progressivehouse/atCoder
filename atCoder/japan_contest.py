def p_a():
    M, D = map(int, input().split())
    ans = 0

    for m in range(M + 1):
        for d in range(D + 1):
            d1 = d // 10
            d2 = d - 10 * d1

            if d1 >= 2 and d2 >= 2 and m == d1 * d2:
                ans += 1

    print(ans)


def p_b():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    mod = 10 ** 9 + 7
    ans = 0

    l = []
    r = []
    for i in range(N):
        lc = 0
        rc = 0
        for j in range(N):
            if A[i] > A[j]:
                if i > j:
                    lc += 1
                else:
                    rc += 1
        l.append(lc)
        r.append(rc)

    an = K * (K + 1) // 2 % mod
    for i in range(N):
        sum_r = an * r[i]
        sum_l = (an - K) * l[i]
        ans += sum_r + sum_l
        ans %= mod

    print(ans)


def p_c():
    N = int(input())
    S = input()
    ans = 2
    for i in range(2 * N):
        if S[i] == "W":
            continue
        l = i - 1
        while l >= 0 and S[l] != "W":
            l -= 1

        r = i + 1
        while r < N and S[r] != "W":
            r += 1

        if l >= 0:
            ans *= i - l + 1
        if r < 2 * N:
            ans *= r - i + 1

    print(ans)


def p_d():
    N = int(input())


if __name__ == '__main__':
    p_d()
