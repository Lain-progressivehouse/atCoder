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

    for i in range(num_v):
        for edge in edges:
            if dist[edge[1] - 1] > dist[edge[0] - 1] + edge[2]:
                dist[edge[1] - 1] = dist[edge[0] - 1] + edge[2]
                if i == num_v - 1 and ans != dist[end - 1]:
                    return -1
        if i == num_v - 2:
            ans = dist[end - 1]

    return ans


def abc061_d():
    n, m = map(int, input().split())
    edges = []
    for _ in range(m):
        a, b, c = map(int, input().split())
        edges.append((a, b, -c))

    ans = bellman_ford(edges, n, 1, n)
    print(-ans if ans != -1 else "inf")


if __name__ == '__main__':
    abc061_d()
