# Dijkstra Shortest Path Algorithm

- Shortest path algorithm
- Single source (will only calculate shortest path from A to all other vertices)
- Does not work on
  - Negative weights
  - Negative cycles
- Greedy algorithm

## Approaches

### Priority Queue

```py
def dijkstra(n, edges, src):
  adj = {}
  dist = {}

  for i in range(n):
    adj[i] = []
    dist[i] = float("inf")
  
  dist[src] = 0

  for x, y, w in edges:
    adj[x].append((y, w))


  heap = deque([(0, src)])

  while heap:
    w, n = heappop(heap)

    for cw, c in adj[n]:
      if w + cw < dist[c]:
        dist[c] = w + cw
        heappush(heap, (dist[c], c))

  return dist

```