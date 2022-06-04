# https://www.geeksforgeeks.org/dijkstras-algorithm-for-adjacency-list-representation-greedy-algo-8/
from collections import defaultdict


class Heap():

    def __init__(self):
        self.array = []
        self.size = 0
        self.pos = []

    def newMinHeapNode(self, v, dist):
        minHeapNode = [v, dist]
        return minHeapNode

    def swapMinHeapNode(self, a, b):
        t = self.array[a]
        self.array[a] = self.array[b]
        self.array[b] = t

    def minHeapify(self, idx):
        smallest = idx
        left = 2 * idx + 1
        right = 2 * idx + 2

        if left < self.size and self.array[left][1] \
                < self.array[smallest][1]:
            smallest = left

        if right < self.size and self.array[right][1] \
                < self.array[smallest][1]:
            smallest = right

        if smallest != idx:
            self.pos[self.array[smallest][0]] = idx
            self.pos[self.array[idx][0]] = smallest

            self.swapMinHeapNode(smallest, idx)

            self.minHeapify(smallest)

    def extractMin(self):
        if self.isEmpty():
            return

        root = self.array[0]

        lastNode = self.array[self.size - 1]
        self.array[0] = lastNode

        self.pos[lastNode[0]] = 0
        self.pos[root[0]] = self.size - 1

        self.size -= 1
        self.minHeapify(0)

        return root

    def isEmpty(self):
        return True if self.size == 0 else False

    def decreaseKey(self, v, dist):
        i = self.pos[v]
        self.array[i][1] = dist

        while i > 0 and self.array[i][1] < self.array[(i - 1) // 2][1]:
            self.pos[self.array[i][0]] = (i - 1) // 2
            self.pos[self.array[(i - 1) // 2][0]] = i
            self.swapMinHeapNode(i, (i - 1) // 2)

            i = (i - 1) // 2

    def isInMinHeap(self, v):
        if self.pos[v] < self.size:
            return True

        return False


class Graph():

    def __init__(self, V):
        self.V = V
        self.graph = defaultdict(list)

    def addEdge(self, src, dest, weight):
        newNode = [dest, weight]
        self.graph[src].insert(0, newNode)

        newNode = [src, weight]
        self.graph[dest].insert(0, newNode)

    def dijkstra(self, src):
        V = self.V
        dist = []

        minHeap = Heap()

        for v in range(V):
            dist.append(float('inf'))
            minHeap.array.append(minHeap.newMinHeapNode(v, dist[v]))
            minHeap.pos.append(v)

        minHeap.pos[src] = src
        dist[src] = 0
        minHeap.decreaseKey(src, dist[src])

        minHeap.size = V

        while not minHeap.isEmpty():
            newHeapNode = minHeap.extractMin()
            u = newHeapNode[0]

            for pCrawl in self.graph[u]:
                v = pCrawl[0]

                if minHeap.isInMinHeap(v) and dist[u] != float('inf') and pCrawl[1] + dist[u] < dist[v]:
                    dist[v] = pCrawl[1] + dist[u]

                    minHeap.decreaseKey(v, dist[v])

        return dist


for _ in range(int(input())):
    n, m = map(int, input().split())
    ts = set(map(lambda x: int(x) - 1, input().split()))

    graph = Graph(n)

    p = int(input())

    for _ in range(p):
        r, s = map(int, input().split())
        r -= 1
        s -= 1

        if (r in ts) and (s in ts):
            graph.addEdge(r, s, 1)

    a, b = map(int, input().split())
    a -= 1
    b -= 1

    x = graph.dijkstra(a)[b]

    if x == float('inf'):
        x = -1

    print(x)
