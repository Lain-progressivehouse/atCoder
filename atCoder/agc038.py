def p_a():
    H, W, A, B = map(int, input().split())

    S = [[0] * W for _ in range(H)]

    if A == 0 and B == 0:
        for i in range(H):
            print(*S[i], sep="")
        exit()

    for i in range(B):
        for j in range(A):
            S[i][j] = 1

    for i in range(B, H):
        for j in range(A, W):
            S[i][j] = 1

    for i in range(H):
        print(*S[i], sep="")


def p_b():
    N, K = map(int, input().split())
    P = list(map(int, input().split()))

    ans = 1
    for i in range(N - K):
        L = sorted(P[i: i + K + 1])
        if P[i] != L[0] or P[i + K] != L[-1]:
            ans += 1

    print(ans)


# from math import gcd
from fractions import gcd


def p_c():
    N = int(input())
    A = list(map(int, input().split()))

    ans = 0

    for i in range(N):
        for j in range(i + 1, N):
            g = gcd(A[i], A[j])
            l = A[i] * A[j] // g
            # print("GCD: {}".format(g))
            # print("LCM: {}".format(l))
            ans += l
            ans %= 998244353

    print(ans)


if __name__ == '__main__':
    p_b()
