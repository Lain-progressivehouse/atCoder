def p_a():
    d = int(input())
    print("Christmas" + " Eve" * (25 - d))


def p_b():
    n = int(input())
    ans = []
    for _ in range(n):
        ans.append(int(input()))
    print(sum(ans) - max(ans) + max(ans) // 2)


def p_c():
    n, k = map(int, input().split())
    H = [int(input()) for _ in range(n)]
    H.sort()
    ans = 10 ** 9 + 1
    for i in range(n - k + 1):
        ans = min(ans, H[i + k - 1] - H[i])
    print(ans)


def p_d():
    n, x = map(int, input().split())
    b, p = [1], [1]
    for i in range(n):
        b.append(b[i] * 2 + 3)
        p.append(p[i] * 2 + 1)

    def solve(n, x):
        if n == 0:
            return 0 if x <= 0 else 1
        elif x <= 1 + b[n - 1]:
            return solve(n - 1, x - 1)
        else:
            return p[n - 1] + 1 + solve(n - 1, x - 2 - b[n - 1])

    print(solve(n, x))


if __name__ == '__main__':
    p_d()
