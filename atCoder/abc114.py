def p_a():
    n = int(input())
    print("YES" if n == 7 or n == 5 or n == 3 else "NO")


def p_b():
    s = input()
    ans = 10 ** 9 + 7
    for i in range(len(s) - 2):
        ans = min(ans, abs(753 - int(s[i:i + 3])))
    print(ans)


def p_c():
    import sys
    sys.setrecursionlimit(10 ** 9)
    n = int(input())

    def dfs(s):
        """
        :type s: str
        """
        if int(s) > n:
            return 0
        ret = 1 if all(s.count(c) for c in "753") else 0
        for c in "753":
            ret += dfs(s + c)
        return ret

    print(dfs("0"))


def prime_factorize(n):
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    return a


def p_d():
    from collections import Counter
    N = int(input())
    li = []
    for i in range(1, N + 1):
        li.extend(prime_factorize(i))
    prime_list = Counter(li).values()

    def num(m):
        return len(list(filter(lambda x: x >= m - 1, prime_list)))

    print(num(75) + num(25) * (num(3) - 1) + num(15) * (num(5) - 1) + num(5) * (num(5) - 1) * (num(3) - 2) // 2)


if __name__ == '__main__':
    p_d()
