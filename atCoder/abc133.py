def p_a():
    N, A, B = map(int, input().split())
    print(min(N * A, B))


import math


def p_b():
    N, D = map(int, input().split())
    X = [list(map(int, input().split())) for _ in range(N)]

    ans = 0
    for i in range(N):
        for j in range(i + 1, N):
            d = sum([(X[i][k] - X[j][k]) ** 2 for k in range(D)])
            if math.sqrt(d).is_integer():
                ans += 1
    print(ans)


def p_c():
    L, R = map(int, input().split())
    year = 2019

    if R - L >= year:
        print(0)
        exit()

    ans = year
    for i in range(L, R + 1):
        for j in range(i + 1, R + 1):
            ans = min(ans, (i * j) % year)
            if ans == 0:
                print(0)
                exit()

    print(ans)


def p_d():
    N = int(input())
    A = list(map(int, input().split()))

    # top = (N + 1) // 2
    # a1 = 0
    # for i in range(top):
    #     if i == top - 1:
    #         a1 += A[i] * ((-1) ** i)
    #     else:
    #         a1 += (A[i] + A[~i]) * ((-1) ** i)
    a1 = sum(A[0::2]) - sum(A[1::2])

    ans = []
    ans.append(a1)
    for i in range(N - 1):
        x = A[i] - ans[i] // 2
        ans.append(x * 2)

    print(*ans)


def p_e():
    N, K = map(int, input().split())
    ab = [tuple(map(int, input().split())) for _ in range(N - 1)]


if __name__ == '__main__':
    p_d()
