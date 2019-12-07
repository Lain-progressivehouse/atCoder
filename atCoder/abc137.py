def p_a():
    a, b = map(int, input().split())
    a1 = a * b
    a2 = a + b
    a3 = a - b

    print(max([a1, a2, a3]))


def p_b():
    a, b = map(int, input().split())

    ans = []
    for i in range(b - a + 1, b + a):
        ans.append(str(i))

    print(" ".join(ans))


from collections import Counter


def p_c():
    n = int(input())
    ans = 0

    l = ["".join(sorted(input())) for _ in range(n)]

    a = Counter(l).values()

    for i in a:
        ans += sum(range(i))

    print(ans)


from heapq import heappop, heappush


def p_d():
    n, m = map(int, input().split())
    ab = [tuple(map(int, input().split())) for _ in range(n)]

    ab.sort()
    ans = 0
    j = 0
    H = []

    for i in range(1, m + 1):
        while j < n and ab[j][0] <= i:
            heappush(H, -ab[j][1])
            j += 1

        if H:
            ans -= heappop(H)

    print(ans)


def bellman_ford(edges, num_v, start, end):
    """
    ベルマンフォード法
    :param edges: (from, to, cost)のリスト
    :param num_v: 頂点の数
    :param start: 始点
    :param end: 終点
    :return: 最小コスト
    """
    inf = float("inf")
    dist = [inf] * num_v
    dist[start - 1] = 0
    ans = -1

    for i in range(num_v * 2):
        for edge in edges:
            if dist[edge[1] - 1] > dist[edge[0] - 1] + edge[2]:
                dist[edge[1] - 1] = dist[edge[0] - 1] + edge[2]
                if i > num_v:
                    dist[edge[1] - 1] = inf
        if i == num_v - 1:
            ans = dist[end - 1]
    if dist[-1] != ans or dist[-1] == -inf:
        return -1
    return max(dist[-1], 0)


def p_e():
    N, M, P = map(int, input().split())
    edges = []
    for _ in range(M):
        a, b, c = map(int, input().split())
        edges.append((a, b, c - P))
    ans = bellman_ford(edges, N, 1, N)
    print(ans)


if __name__ == '__main__':
    p_e()
