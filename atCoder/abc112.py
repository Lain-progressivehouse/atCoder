def p_a():
    n = int(input())
    if n == 1:
        print("Hello World")
    else:
        a = int(input())
        b = int(input())
        print(a + b)


def p_b():
    N, T = map(int, input().split())
    ans = 10 ** 9
    for _ in range(N):
        c, t = map(int, input().split())
        if t <= T:
            ans = min(ans, c)
    print(ans if ans != 10 ** 9 else "TLE")


def p_c():
    from itertools import product
    N = int(input())
    xyh = [tuple(map(int, input().split())) for _ in range(N)]
    for x, y in product(range(101), repeat=2):
        high = xyh[0][2] + abs(xyh[0][0] - x) + abs(xyh[0][1] - y)
        if all(h == max(0, high - abs(x - i) - abs(y - j)) for i, j, h in xyh):
            print(x, y, high)


def p_d():
    pass


if __name__ == '__main__':
    p_c()
