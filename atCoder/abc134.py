def p_a():
    print(int(input()) ** 2 * 3)


def p_b():
    n, d = map(int, input().split())
    i = 2 * d + 1
    print((n + i - 1) // i)


def p_c():
    N = int(input())
    A = [int(input()) for _ in range(N)]

    m = max(A)
    a = A.index(m)
    A.pop(a)
    b = max(A)

    for i in range(N):
        if i == a:
            print(b)
        else:
            print(m)


def p_d():
    N = int(input())
    A = list(map(int, input().split()))
    B = [0] * N
    ans = []

    for i in reversed(range(1, N + 1)):
        target = N // i
        v = sum([B[i * j - 1] for j in range(1, target + 1)])
        if v % 2 != A[i - 1]:
            B[i - 1] = 1
            ans.append(i)

    print(len(ans))
    if ans:
        print(" ".join(map(str, ans)))


from bisect import *


def p_e():
    N = int(input())
    # A = [int(input()) for _ in range(N)]
    ans = [-1] * N

    for _ in range(N):
        a = int(input())
        ans[bisect(ans, a - 1) - 1] = a

    print(N - bisect(ans, -1))


if __name__ == '__main__':
    p_e()
