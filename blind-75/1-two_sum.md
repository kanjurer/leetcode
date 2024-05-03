# Problem 1: Two Sum

## Solution

```java
// O(n) time, O(n) space
class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> map = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            if (map.containsKey(target - nums[i])) {
                return new int[] { map.get(target - nums[i]), i };
            }
            map.put(nums[i], i);
        }

        return null;
    }
}
```

## Notes

We are storing index of each number in the map. Then, we check if the complement of the current number is in the map. If it is, we return the indices. Otherwise, we add the current number to the map.

## Questions to interviewer

1. What if there are multiple solutions?
2. What if there are no solutions?
3. Do we have to return the indices in sorted order?
4. Can I assume that the array is sorted? (This is a good question to ask for every problem)
5. Do we need O(1) space complexity or can I use additional space? (This is a good question to ask for every problem)
