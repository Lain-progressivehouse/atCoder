def p_a():
    i = int(input())
    print(i ** 3)


def p_b():
    N = int(input())
    A = list(map(int, input().split()))
    A = [i - 1 for i in A]
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))

    ans = 0

    bf = -100
    for i in A:
        ans += B[i]
        if bf == i - 1:
            ans += C[i - 1]
        bf = i

    print(ans)


def p_c():
    N = int(input())
    B = list(map(int, input().split()))

    A = []
    A.append(B[0])

    for i in range(0, N - 2):
        A.append(min(B[i], B[i + 1]))

    A.append(B[-1])

    print(sum(A))


def p_d():
    N, K = map(int, input().split())
    S = input()
    ans = 0

    for n in range(N - 1):
        if S[n] == S[n + 1]:
            ans += 1

    np = N - ans - 1

    for k in range(K):
        if np > 1:
            ans += 2
            np -= 2
        elif np == 1:
            ans += 1
            np -= 1

    print(ans)


"""
未AC
"""


def p_e():
    N = int(input())
    P = list(map(int, input().split()))
    n = N - 1

    ans = n * (n + 1) * (2 * n + 1) // 6

    for i in range(N):
        if not (P[i] == i + 1 or P[i] == N - i):
            ans -= 1

    print(ans)


if __name__ == '__main__':
    p_e()
