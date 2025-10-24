### DFS

```py
def topological_sort(edges):
    adj = defaultdict(list)
    for x, y in edges:
        adj[x].append(y)

    visited = set()
    stack = []

    def dfs(node):
        visited.add(node)
        for c in adj[node]:
            if c not in visited:
                dfs(c)
        stack.append(node)

    for node in adj:
        if node not in visited:
            dfs(node)

    return stack[::-1]
```

### BFS

```py
def topological_sort(edges):
    adj = defaultdict(list)
    indegree = defaultdict(int)

    for x, y in edges:
        adj[x].append(y)
        indegree[y] += 1

    q = deque()

    for node, indeg in indegree.items():
        if indeg == 0: q.append(node)

    result = []

    while q:
        n = q.popleft()
        result.append(n)

        for c in adj[n]:
            indegree[c] -= 1
            if indegree[c] == 0: q.append(c)

    return result
```
