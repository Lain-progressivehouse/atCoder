def p_a():
    k, x = map(int, input().split())
    print("Yes" if 500 * k >= x else "No")


def p_b():
    n = int(input())
    s = input()
    ans = 0
    for i in range(n - 2):
        if "ABC" == s[i:i + 3]:
            ans += 1
    print(ans)


def p_c():
    from itertools import permutations
    N = int(input())
    st_list = "".join(map(str, range(1, N + 1)))
    *P, = map(int, input().split())
    *Q, = map(int, input().split())
    *per, = permutations(range(1, N + 1))
    per.sort()
    li = []
    for p in per:
        li.append("".join(map(str, p)))
    p = "".join(map(str, P))
    q = "".join(map(str, Q))
    print(abs(li.index(q) - li.index(p)))


def p_d():
    from fractions import gcd
    n, m = map(int, input().split())
    *A, = map(lambda x: int(x) // 2, input().split())

    c = 0
    for a in A:
        if c == 0:
            while a & 1 == 0:
                c += 1
                a >>= 1
        else:
            ne = 0
            while a & 1 == 0:
                ne += 1
                a >>= 1
            if c != ne:
                print(0)
                exit()

    lcm = A[0]
    for i in range(1, n):
        lcm = lcm * A[i] // gcd(lcm, A[i])
    print((m // lcm + 1) // 2)


def p_e():
    N = int(input())
    *C, = map(int, input().split())
    C.sort()
    mod = 10 ** 9 + 7
    ans = 0
    for i in range(N):
        ans += C[i] * (i + 1)
        ans %= mod
    print((4 << (N - 1)) * ans % mod)


def p_f():
    pass


if __name__ == '__main__':
    p_d()
