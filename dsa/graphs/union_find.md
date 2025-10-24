# Union Find

## Introduction

Union Find is comprised of:

- start with a set of disjoint sets
- merge sets together and find parent of a set

```py
class UF:
    def __init__(self, n):
        self.parent = {}
        self.size = {}

        for i in range(n):
            self.parent[i] = i
            self.size[i] = 1

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x != y:
            if self.size[x] < self.size[y]:
                x, y = y, x
            self.parent[y] = x
            self.size[x] += self.size[y]

    def find(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
```
