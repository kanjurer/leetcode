# Python

This is a collection of Python tips and tricks that I have found useful.

## Table of Contents

- Useful Functions
  - Enumerate
  - Divmod
  - Any and All
- Data Structures
  - Sets

## Useful Functions

### Range

The `range()` function is used to generate a sequence of numbers.

```py
# Generate numbers from 0 to 4
range(5) # [0, 1, 2, 3, 4]

# Generate numbers from 1 to 5
range(1, 6) # [1, 2, 3, 4, 5]

# Generate numbers from 1 to 10 with a step of 2
range(1, 11, 2) # [1, 3, 5, 7, 9]

# Generate numbers from 10 to 1 with a step of -1
range(10, 0, -1) # [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
```

### Zip

The `zip()` function is used to combine two or more iterables into a single iterable of tuples.

```py
nums = [1, 2, 3]
fruits = ['apple', 'banana', 'cherry']

for num, fruit in zip(nums, fruits):
    print(num, fruit)

"""
Output:
1 apple
2 banana
3 cherry
"""
```

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

### Any and All

The `any()` function returns `True` if any of the elements in the iterable are `True`, and `False` otherwise.
The `all()` function returns `True` if all of the elements in the iterable are `True`, and `False` otherwise.

```py
nums = [1, 2, 3, 4, 5]
all(nums) # True
any(nums) # True

nums = [0, 0, 0, 0, 0]
all(nums) # False
any(nums) # False

nums = [1, 0, 0, 0, 0]
all(nums) # False
any(nums) # True
```

### Filter

The `filter()` function is used to filter out elements from an iterable based on a function that returns `True` or `False`.

```py
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_nums = list(filter(lambda x: x % 2 == 0, nums))
print(even_nums)

"""
Output:
[2, 4, 6, 8, 10]
"""
```

## Strings

### Indexing

```py
s = "Hello, World!"
s[0] # H
s[-1] # !
s[:5] # Hello
s[7:9] # Wo
s[::-1] # !dlroW ,olleH
```

### isalnum

The `isalnum()` method returns `True` if all characters in the string are alphanumeric (either alphabets or numbers), and there is at least one character, `False` otherwise.

```py
print("Hello123".isalnum()) # True
print("Hello 123".isalnum()) # False
print("Hell$o".isalnum()) # False
```

### join

The `join()` method is used to join the elements of an iterable (such as a list) into a string.

```py
fruits = ['apple', 'banana', 'cherry']
print(', '.join(fruits)) # apple, banana, cherry
print(''.join(fruits)) # applebananacherry
```

### split

The `split()` method is used to split a string into a list of substrings based on a delimiter.

```py
sentence = "Hello, World!"
words = sentence.split()
print(words) # ['Hello,', 'World!']

sentence = "apple,banana,cherry"
fruits = sentence.split(',')
print(fruits) # ['apple', 'banana', 'cherry']
```

## Data Structures

### Sets

The `set()` function is used to create a set.

```py
# Create an empty set
empty_set = set()

# Create a set with elements
fruits = set(['apple', 'banana', 'cherry', 'apple'])
print(fruits)

"""
Output:
{'apple', 'banana', 'cherry'}
"""
```
