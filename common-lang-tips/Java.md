# Java

This is a collection of Java tips and tricks that I have found useful.

## Hash Maps

To check if a key exists, use:

```java
map.containsKey(key); // better

// or

map.get(key) != null;
```

## Collections

To convert Collection to List

```java
Collection<Integer> c = new ArrayList<>();

List<Integer> l = new ArrayList<>(c);
```

# Strings

To convert string to character array

```java
char[] arr = s.toCharArray();
```
