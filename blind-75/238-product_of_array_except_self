# Problem 238: Product of Array Except Self

## Solution

```java
class Solution {
    public int[] productExceptSelf(int[] nums) {
        int n = nums.length;
        int[] ans = new int[n];

        int prod = 1;

        for(int i = 0; i < n; i++){
            ans[i] = prod;
            prod = prod * nums[i];
        }

        prod = 1;

        for(int i = n-1; i >=0; i--){
            ans[i] = ans[i] * prod;
            prod = prod * nums[i];
        }

        return ans;
    }
}
```

## Notes

We use a trick. In the first pass, we store all the prefixes here (prefix of i is product of all numbers before ith number). In the second pass, instead of storing suffixes in a separate array, we just multiply the prefix array with suffixes as we go along to save space (we use a variable called prod to keep track of running product)

## Questions to interviewer

1. Can we assume that the product of all numbers in the array will fit in an int?
2. Can we use additional space?
3. Can we modify the input array, or should I create a new array to store the output?
