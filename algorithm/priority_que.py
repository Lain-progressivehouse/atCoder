class PriorityQue:
    def __init__(self, max_size=10 ** 5):
        self.heap = [0] * max_size
        self.size = 0

    def push(self, x):
        i = self.size
        self.size += 1
        # 自分のノードの番号

        while i > 0:
            # 親ノードの番号
            p = (i - 1) // 2

            # 番号が逆転していないなら抜ける
            if self.heap[p] <= x:
                break

            # 親ノードの数字を下ろして、自分は上に
            self.heap[i] = self.heap[p]
            i = p
        self.heap[i] = x

    def pop(self):
        # 最小値
        ret = self.heap[0]

        # 根に持ってくる値
        self.size -= 1
        x = self.heap[self.size]

        # 根から下ろしていく
        i = 0
        while i * 2 + 1 < self.size:
            # 子同士を比較
            a = i * 2 + 1
            b = i * 2 + 2
            if b < self.size and self.heap[b] < self.heap[a]:
                a = b

            # もう逆転していないなら終わる
            if self.heap[a] >= x:
                break

            # この数字を持ち上げる
            self.heap[i] = self.heap[a]
            i = a

        self.heap[i] = x

        return ret
