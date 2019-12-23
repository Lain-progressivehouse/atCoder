def p_a():
    a = int(input())
    b = int(input())
    print(6 - a - b)


def p_b():
    n = int(input())
    s, t = input().split()
    ans = ""
    for i in range(n):
        ans += s[i]
        ans += t[i]
    print(ans)


def p_c():
    from fractions import gcd
    a, b = map(int, input().split())
    print(a * b // gcd(a, b))


def p_d():
    n = int(input())
    A = map(int, input().split())
    st = 1
    ans = n
    for a in A:
        if a == st:
            st += 1
            ans -= 1
    print(ans if n != ans else -1)


def p_e():
    n = int(input())
    if n & 1 == 1:
        print(0)
        exit()
    ans = n // 10
    x = 50
    while x <= n:
        ans += n // x
        x *= 5
    print(ans)


def p_f():
    from sys import stdin
    input = stdin.readline
    N, u, v = map(int, input().split())
    edges = [list(map(int, input().split())) for i in range(N - 1)]
    if u == v:
        print(0)
        exit()

    def BFS(K, edges, N):
        roots = [[] for i in range(N)]
        for a, b in edges:
            roots[a - 1] += [(b - 1, 1)]
            roots[b - 1] += [(a - 1, 1)]
        dist = [-1] * N
        stack = []
        stack.append(K)
        dist[K] = 0
        while stack:
            label = stack.pop(-1)
            for i, c in roots[label]:
                if dist[i] == -1:
                    dist[i] = dist[label] + c
                    stack += [i]
        return dist

    dist_v = BFS(v - 1, edges, N)
    dist_u = BFS(u - 1, edges, N)
    # print(dist_v)
    # print(dist_u)
    max_dist = max(dist_v)
    maxIndex = [i for i, x in enumerate(dist_v) if x == max_dist]
    for i in maxIndex:
        if max_dist > dist_u[i]:
            print(max(dist_v) - 1)
            exit()
    if dist_v[u - 1] > max_dist - dist_v[u - 1]:
        print(max_dist - 1)
    else:
        print(dist_v[u - 1] - 1)


if __name__ == '__main__':
    p_f()
