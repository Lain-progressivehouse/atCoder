def p_a():
    import string
    l = string.ascii_lowercase
    c = input()
    print(l[l.index(c) + 1])


def p_b():
    n, k, m = map(int, input().split())
    *A, = map(int, input().split())
    ans = max(n * m - sum(A), 0)
    print(ans if k >= ans else -1)


def p_c():
    from collections import defaultdict
    d = defaultdict(int)
    ac_list = set()
    n, m = map(int, input().split())
    for _ in range(m):
        p, s = input().split()
        if s == "WA" and p not in ac_list:
            d[p] += 1
        if s == "AC":
            ac_list.add(p)
    wa = 0
    for key in d.keys():
        if key in ac_list:
            wa += d[key]
    print(len(ac_list), wa)


def p_d():
    from itertools import product
    h, w = map(int, input().split())
    maze = [input for _ in range(h)]
    for i, j in product(range(h), range(w)):
        if maze[i][j] == "#":
            continue
        dp = [[-1] * w for _ in range(h)]
        


def p_e():
    pass


def p_f():
    pass


if __name__ == '__main__':
    p_c()
