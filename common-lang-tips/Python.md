# Python

This is a collection of Python tips and tricks that I have found useful.

### Enumerate

The `enumerate()` function is used to iterate over a list and keep track of the index of the current item. It returns a tuple containing the index and the item at that index.

```py
nums = ['apple', 'banana', 'cherry']

for i, num in enumerate(nums):
    print(i, num)

"""
Output:
0 apple
1 banana
2 cherry
"""
```

### Divmod

The `divmod()` function returns a tuple containing the quotient and the remainder when dividing two numbers.

```py
quotient, remainder = divmod(10, 3)
print(quotient, remainder)

"""
Output:
3 1
"""
```
