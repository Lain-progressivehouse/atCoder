def p_a():
    s, t = input().split()
    print(t + s)


def p_b():
    a, b, k = map(int, input().split())
    if a >= k:
        a -= k
    else:
        b -= k - a
        b = max(0, b)
        a = 0
    print(a, b)


def p_c():
    n = int(input())

    def primes(n):
        is_prime = [True] * (n + 1)
        is_prime[0] = False
        is_prime[1] = False
        for i in range(2, int(n ** 0.5) + 1):
            if not is_prime[i]:
                continue
            for j in range(i * 2, n + 1, i):
                is_prime[j] = False
        return [i for i in range(n + 1) if is_prime[i]]

    li = primes(n * 2)

    for i in range(n, n * 2):
        if i in li:
            print(i)
            exit()


def p_d():
    N, K = map(int, input().split())
    *rsp, = map(int, input().split())
    li = {
        "r": 0,
        "s": 1,
        "p": 2
    }
    t = input()
    ans = 0
    for k in range(K):
        dp = [0] * 3
        for i in range(k, N, K):
            x = li[t[i]]
            NEXT = [0] * 3
            for p in range(3):
                NEXT[p] = max(dp[(p + 1) % 3], dp[(p - 1) % 3])
                if (p + 1) % 3 == x:
                    NEXT[p] += rsp[p]
            dp = NEXT
        ans += max(dp)
    print(ans)


def p_e():
    from itertools import accumulate
    n, m = map(int, input().split())
    *A, = map(int, input().split())
    A.sort(reverse=True)
    ls = [0] * 10 ** 6
    for a in A:
        ls[a + 1] += 1
    ls = list(accumulate(ls))

    def check(x):
        res = 0
        for a in A:
            res += n - ls[max(0, x - a)]
        return res

    up = 10 ** 6
    down = 0
    while True:
        mid = (up + down) // 2
        if check(mid) >= m:
            if down == mid:
                break
            down = mid
        else:
            if up == mid:
                if check(up) == m:
                    mid == up
                break
            up = mid
    acc_ls = list(accumulate([0] + A))
    ans = 0
    for a in A:
        x = n - ls[max(0, mid - a)]
        ans += x * a + acc_ls[x]
    print(ans - (check(mid) - m) * mid)


def p_f():
    pass


if __name__ == '__main__':
    p_e()
