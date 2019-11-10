def p_a():
    a, b = map(int, input().split())
    print(0 if a < 6 else b if a > 12 else b // 2)


def p_b():
    r, d, x = map(int, input().split())
    for _ in range(10):
        x = r * x - d
        print(x)


def p_c():
    n, m = map(int, input().split())
    _min = n
    _max = 0
    for _ in range(m):
        l, r = map(int, input().split())
        _min = min(_min, r)
        _max = max(_max, l)
    print(max(_min - _max + 1, 0))


from heapq import heappop, heappush, heapify


def p_d():
    n, m = map(int, input().split())
    *h, = map(int, input().split())
    heapify(h)
    bc = [tuple(map(int, input().split())) for _ in range(m)]
    bc.sort(key=lambda x: x[1], reverse=True)
    for b, c in bc:
        for i in range(b):
            tmp = heappop(h)
            if tmp >= c:
                heappush(h, tmp)
                print(sum(h))
                exit()
            heappush(h, c)
    print(sum(h))


def p_e():
    pass


def p_f():
    pass


if __name__ == '__main__':
    p_d()
