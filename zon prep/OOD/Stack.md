# Design a Stack

```py
from typing import TypeVar, Generic

T = TypeVar('T')

class Stack(Generic[T]):
    items: list[T]

    def __init__(self) -> None:
        self.items = []

    def push(self, item: T) -> None:
        self.items.append(item)

    def pop(self) -> T:
        return self.items.pop()

    def empty(self) -> bool:
        return not self.items

# Usage
stack = Stack[int]()
stack.push(1)
stack.push(2)
print(stack.pop())  # Output: 2
```
