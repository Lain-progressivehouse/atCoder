def p_a():
    a, b = map(int, input().split())
    if b > a:
        a, b = b, a
    print(a + max(a - 1, b))


def p_b():
    n = int(input())
    *H, = map(int, input().split())
    c = 0
    ans = 0
    for h in H:
        if c <= h:
            c = h
            ans += 1
    print(ans)


def p_c():
    *S, = map(int, input())
    ans = [0] * 2
    for i, s in enumerate(S):
        ans[(i + s) % 2] += 1
    print(min(ans))


def p_d():
    n, k = map(int, input().split())
    *s, = map(int, input())
    ans = 0
    l, r = 0, 0
    count = 0
    while r < n:
        while r < n and count < k:
            if s[r] == 0:
                count += 1
                while r < n and s[r] == 0:
                    r += 1
            else:
                while r < n and s[r] == 1:
                    r += 1
        while r < n and s[r] == 1:
            r += 1
        ans = max(ans, r - l)
        while l < r and s[l] == 1:
            l += 1
        while l < r and s[l] == 0:
            l += 1
        count -= 1

    print(ans)


if __name__ == '__main__':
    p_d()
