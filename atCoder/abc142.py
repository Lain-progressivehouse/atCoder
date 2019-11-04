from sys import stdin

input = stdin.readline


def p_a():
    n = int(input())
    print(((n + 1) // 2) / n)


def p_b():
    n, k = map(int, input().split())
    h = list(map(int, input().split()))

    print(sum(map(lambda x: x >= k, h)))


def p_c():
    n = int(input())
    k = list(map(int, input().split()))

    print(*[i[0] for i in sorted(enumerate(k, start=1), key=lambda x: x[1])])


def calc_gcd(a, b):
    return calc_gcd(b, a % b) if b else a


def p_d():
    a, b = map(int, input().split())
    gcd = calc_gcd(a, b)
    ans = 1
    cnt = 2
    # 素因数分解
    while cnt * cnt < gcd:
        up = True
        while gcd % cnt == 0:
            if up:
                ans += 1
                up = False
            gcd //= cnt
        cnt += 1
    ans += 1 if gcd != 1 else 0
    print(ans)


def p_e():
    N, M = map(int, input().split())
    max_value = (10 ** 5) * 12 + 1
    dp_len = 1 << N
    dp = [max_value] * dp_len
    dp[0] = 0
    for _ in range(M):
        a, b = map(int, input().split())
        keys = list(map(int, input().split()))
        index = 0
        for key in keys:
            index += 2 ** (key - 1)

        for i in range(dp_len):
            if dp[i] == max_value:
                continue
            dp_index = i | index
            dp[dp_index] = min(dp[dp_index], dp[i] + a)

    print(dp[-1] if dp[-1] != max_value else -1)


if __name__ == '__main__':
    p_e()
