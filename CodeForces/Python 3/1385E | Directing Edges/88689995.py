from collections import defaultdict
from sys import setrecursionlimit
 
setrecursionlimit(10 ** 9)
 
 
def topological_sort(graph, start):
    seen = set()
    stack = []
    order = []
    q = [start]
    while q:
        v = q.pop()
        if v not in seen:
            seen.add(v)
            q.extend(graph[v])
 
            while stack and v not in graph[stack[-1]]:
                order.append(stack.pop())
            stack.append(v)
 
    return stack + order[::-1]
 
 
class Graph():
    def __init__(self, vertices):
        self.graph = defaultdict(list)
        self.V = vertices
 
        self.visited = [False] * self.V
        self.recStack = [False] * self.V
 
    def addEdge(self, u, v):
        self.graph[u].append(v)
 
    def isCyclicUtil(self, v):
        try:
            self.visited[v] = True
            self.recStack[v] = True
 
            for neighbour in self.graph[v]:
                if not self.visited[neighbour]:
                    if self.isCyclicUtil(neighbour):
                        return True
                elif self.recStack[neighbour]:
                    return True
 
            self.recStack[v] = False
            return False
 
        except Exception as e:
            pass
 
    def isCyclic(self):
        for node in range(self.V):
            if not self.visited[node]:
                if self.isCyclicUtil(node):
                    return True
 
        return False
 
 
for _ in range(int(input())):
    n, m = map(int, input().split())
 
    graph = [[] for _ in range(n)]
    degrees = [0] * n
 
    dg = Graph(n)
 
    undirected = []
 
    for _ in range(m):
        w, u, v = map(int, input().split())
        u -= 1
        v -= 1
 
        if w:
            dg.addEdge(u, v)
            graph[u].append(v)
            degrees[v] += 1
        else:
            undirected.append((u, v))
 
    if dg.isCyclic():
        print('NO')
        continue
 
    top = []
 
    for u in range(n):
        if degrees[u] == 0:
            top.extend(topological_sort(graph, u))
 
    if not top:
        print('NO')
        continue
 
    d = {}
 
    for i in range(len(top)):
        d[top[i]] = i
 
    for u, v in undirected:
        try:
            if d[u] < d[v]:
                dg.addEdge(u, v)
                graph[u].append(v)
            else:
                dg.addEdge(v, u)
                graph[v].append(u)
        except:
            dg.addEdge(u, v)
            graph[u].append(v)
 
    if dg.isCyclic():
        print('NO')
        continue
 
    print('YES')
 
    for u in range(n):
        for v in graph[u]:
            print(u + 1, v + 1)