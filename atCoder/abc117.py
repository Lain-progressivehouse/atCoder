def p_a():
    t, x = map(int, input().split())
    print(t / x)


def p_b():
    n = int(input())
    *L, = map(int, input().split())
    print("Yes" if max(L) < sum(L) - max(L) else "No")


def p_c():
    n, m = map(int, input().split())
    *X, = map(int, input().split())
    X.sort()
    L = [abs(X[i] - X[i + 1]) for i in range(m - 1)]
    L.sort()
    print(sum(L[:len(L) - n + 1]) if m > n else 0)


def p_d():
    """
    嘘解法
    9 4
    0 0 0 0 0 4 4 4 6
    のとき
    出力: 22
    真の正解: 41
    :return:
    """
    n, k = map(int, input().split())
    *A, = map(int, input().split())
    size = (len(bin(max(A + [k]))) - 2)
    bits = [0] * size
    for a in A:
        for i in range(len(bin(a)) - 2):
            bits[i] += a >> i & 1

    now = 0
    ans = 0
    for i, bit_count in enumerate(reversed(bits)):
        b = 1 << size - i - 1
        if k < now | b or n - bit_count <= bit_count:
            ans += bit_count * b
            continue
        now |= b
        ans += (n - bit_count) * b

    print(ans)


def p_dd():
    x = int(input())
    *A, = map(int, input().split())
    ans = 0
    for a in A:
        ans += a ^ x
    print(ans)


def p_dp():
    n, k = map(int, input().split())
    *A, = map(int, input().split())

    size = (len(bin(max(A + [k]))) - 2)
    bits = [0] * size
    for a in A:
        for i in range(len(bin(a)) - 2):
            bits[i] += a >> i & 1

    # dp[i][j]: 上位iビットまで見たときに、k以下であることが(j?確定:未確定)であるときの最大値
    dp = [[0] * 2 for _ in range(40)]

    # for i in range(40)


if __name__ == '__main__':
    p_dp()
