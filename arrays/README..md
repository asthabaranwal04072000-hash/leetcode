# Two Sum

## Idea

Store previously seen numbers in a hashmap.

For every current number:

- calculate target - current
- if it exists in hashmap
    return previous index and current index
- otherwise store current number and index

Time Complexity: O(n)

Space Complexity: O(n)

# Contains Duplicate

## Idea

- I remembered it today