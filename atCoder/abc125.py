def p_a():
    a, b, t = map(int, input().split())
    print(t // a * b)


def p_b():
    n = int(input())
    *v, = map(int, input().split())
    *c, = map(int, input().split())
    ans = 0
    for a, b in zip(v, c):
        if a - b > 0:
            ans += a - b
    print(ans)


from fractions import gcd


def p_c():
    n = int(input())
    *a, = map(int, input().split())
    L = [0] * n
    R = [0] * n
    for i in range(n - 1):
        L[i] = gcd(L[i - 1], a[i])
        R[n - 1 - i] = gcd(R[(n - i) % n], a[n - 1 - i])
    ans = [gcd(L[i - 1], R[(i + 1) % n]) for i in range(n)]
    print(max(ans))


def p_d():
    n = int(input())
    *a, = map(int, input().split())
    *b, = filter(lambda x: x <= 0, a)
    *c, = map(abs, a)
    if len(b) & 1 == 0:
        print(sum(c))
    else:
        print(sum(c) - 2 * sorted(c)[0])


if __name__ == '__main__':
    p_c()
