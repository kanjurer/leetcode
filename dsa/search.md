# Search

DFS vs BFS

```py

def dfs(node):
    visited = set()

    s = [node]

    while s:
        n = s.pop()
        visited.add(n)

        for c in adj[n]:
            if c not in visited:
                s.append(c)
```

```py
def bfs(node):
    visited = set()

    q = [node]

    while q:
        n = q.popleft()
        visited.add(n)

        for c in adj[n]:
            if c not in visited:
                q.append(c)
```