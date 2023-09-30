# Problem 242: Valid Anagram

## Solution

```java
// O(n) time, O(n) space
class Solution {
    public boolean isAnagram(String s, String t) {
        if(s.length() != t.length()) return false;

        Map<Character, Integer> m = new HashMap<>();

        for(char c : s.toCharArray()){
            if(m.get(c) == null){
                m.put(c, 0);
            }

            m.put(c, m.get(c) + 1);
        }

        for(char c : t.toCharArray()){
            if(m.get(c) == null){
                return false;
            }

            m.put(c, m.get(c) - 1);
        }

        for(int i : m.values()){
            if(i != 0) return false;
        }

        return true;
    }
}

// O(n) time, O(n) space
class Solution {
    public boolean isAnagram(String s, String t) {
        if(s.length() != t.length()) return false;

        char[] sArr = s.toCharArray();
        char[] tArr = t.toCharArray();

        Arrays.sort(sArr);
        Arrays.sort(tArr);

        return Arrays.equals(sArr, tArr);
    }
}
```

## Notes

We create a map that maps each character to the number of times it appears in the first string. Then we iterate through the second string and decrement the count for each character. If the count is ever less than 0, we know that the second string has a character that the first string does not have. If the count is ever greater than 0, we know that the first string has a character that the second string does not have. If the count is ever not 0, we know that the strings are not anagrams. Otherwise, they are anagrams.

Optimizations:

- We can use an array of size 26 instead of a map. This will save us space.
- We can use an array of size 256 for Unicode.

## Questions to interviewer

1. Can the strings have any characters?
2. Can I use additional space?
3. Do you want O(n) time? (I think this is a good question to ask for every problem)
4. Can I assume that the strings are ASCII strings? (This is a good question to ask for every problem)
5. Can I assume that the strings are Unicode strings? (This is a good question to ask for every problem)

what is the time and space complexity of java's arrays.sort() method?
answer is that it is O(nlogn) time and O(1) space. It uses a dual-pivot quicksort algorithm.
