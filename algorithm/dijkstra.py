from heapq import heappop, heappush, heapify


def heapq_dijkstra(cost, num_v, start):
    """
    ダイクストラ法
    :param cost: 隣接行列
    :param num_v: 頂点数
    :param start: 始点
    :return:
    """
    inf = float("inf")
    dist = [(inf if i != start - 1 else 0, i) for i in range(num_v)]
    heapify(dist)
    result = [inf] * num_v
    while dist:
        c, v = heappop(dist)
        next_dist = []
        for f_c, i in dist:
            f_c = min(f_c, c + cost[v][i])
            heappush(next_dist, (f_c, i))
        result[v] = c
        dist = next_dist

    return result


def dijkstra(cost, num_v, start):
    """
    ダイクストラ法
    :param cost: 隣接行列
    :param num_v: 頂点数
    :param start: 始点
    :return:
    """
    inf = float("inf")
    dist = [inf] * num_v
    used = [False] * num_v
    dist[start - 1] = 0
    while True:
        v = -1
        for i in range(num_v):
            if (not used[i]) and (v == -1):
                v = i
            elif (not used[i]) and (dist[i] < dist[v]):
                v = i
        if v == -1:
            break
        used[v] = True

        for i in range(num_v):
            dist[i] = min(dist[i], dist[v] + cost[v][i])
    return dist


def abc035_d():
    n, m, t = map(int, input().split())
    *a, = map(int, input().split())
    inf = float("inf")
    go_cost = [[inf] * n for _ in range(n)]
    re_cost = [[inf] * n for _ in range(n)]
    for _ in range(m):
        f_, t_, c = map(int, input().split())
        go_cost[f_ - 1][t_ - 1] = c
        re_cost[t_ - 1][f_ - 1] = c

    go_route = heapq_dijkstra(go_cost, n, 1)
    re_route = heapq_dijkstra(re_cost, n, 1)
    ans = [_a * (t - go_route[i] - re_route[i]) for i, _a in enumerate(a)]
    print(max(ans))


if __name__ == '__main__':
    abc035_d()
