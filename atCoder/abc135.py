def p_a():
    a, b = map(int, input().split())

    if (a + b) % 2 == 1:
        print("IMPOSSIBLE")
    else:
        print((a + b) // 2)


def p_b():
    N = int(input())
    p_n = list(map(int, input().split()))

    p_sort = sorted(p_n)
    cnt = 0

    for a, b in zip(p_n, p_sort):
        if a != b:
            cnt += 1

    if cnt == 0 or cnt == 2:
        print("YES")
    else:
        print("NO")


def p_c():
    N = int(input())
    A = list(map(int, input().split()))  # N+1の町にモンスターAi体
    B = list(map(int, input().split()))

    ans = 0

    for i in range(N):
        if A[i] >= B[i]:
            A[i] -= B[i]
            ans += B[i]
        else:
            B[i] -= A[i]
            ans += A[i]
            A[i] = 0
            if A[i + 1] >= B[i]:
                A[i + 1] -= B[i]
                ans += B[i]
            else:
                B[i] -= A[i + 1]
                ans += A[i + 1]
                A[i + 1] = 0

    print(ans)


def p_d():
    S = input()
    N = 13

    dp = [0] * N
    dp[0] = 1

    mul = 1
    mod = 10 ** 9 + 7

    for i in reversed(range(len(S))):
        nextDP = [0] * N
        c = S[i]
        if c == "?":
            for k in range(10):  # 数字[0-9]
                for j in range(N):
                    nextDP[(k * mul + j) % N] += dp[j]
                    nextDP[(k * mul + j) % N] %= mod
        else:
            k = int(c)
            for j in range(N):
                nextDP[(k * mul + j) % N] += dp[j]
                nextDP[(k * mul + j) % N] %= mod
        mul *= 10
        mul %= N
        dp = nextDP

    print(int(dp[5]))


if __name__ == '__main__':
    p_d()
