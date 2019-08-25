def p_a():
    S = input()

    i = 0
    nx = ""
    ans = 0
    while i < len(S):
        p = nx
        nx = S[i]

        while p == nx and i + 1 < len(S):
            i += 1
            nx += S[i]

        if i + 1 > len(S):
            break

        i += 1
        ans += 1

    print(ans)


def p_c():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    l = [-1] * N

    for i in range(N):
        l[i] = B[i - 1] + B[(i + 1) % N]

    ans = 0

    while 1:
        f = False
        for i in range(N):
            if A[i] <= B[i] - l[i]:
                f = True
                n = (B[i] - A[i]) // l[i]
                ans += n
                B[i] -= n * l[i]
                l[i - 1] -= n * l[i]
                l[(i + 1) % N] -= n * l[i]
        if not f:
            break

    if A != B:
        print(-1)
    else:
        print(ans)


import numpy as np


def p_d():
    N, M = map(int, input().split())
    A = np.array([list(map(int, input().split())) for _ in range(N)])

    for i in range(1, N + 1):
        print(np.where((A > M * (i - 1)) & (A <= M * i)))


if __name__ == '__main__':
    p_d()
