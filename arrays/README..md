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

#Group Anagram

##Idea

Need a way to make every anagram look identical

Example:
eat
tea
ate

sort every word

aet
aet
aet

use the sorted word as the hashmap key

Hashmap:

"aet" [eat,tea,ate]
Time complexity : O(n * klogk)
Space Complexity : O(n*k)
