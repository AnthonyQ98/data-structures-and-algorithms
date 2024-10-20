# Search Algorithms

## Linear Search
- **Time Complexity**: O(n)
- **Description**: 
  - Iterates through a collection of elements (usually unsorted) in an attempt to find a given item.
  - It is the most basic and easiest form of search, but also the most inefficient.
  - If the collection is sorted, searching is still inefficient when the item is present, but slightly more efficient when the item is not present, as we can stop early if we encounter an item larger than the one we are looking for. However, it still remains O(n) on average.

## Binary Search
- **Time Complexity**: O(log n)
- **Description**:
  - Uses a divide-and-conquer strategy by cutting the collection in half each iteration.
  - Steps:
    1. Check the midpoint. Is it the item?
    2. If not, is the midpoint greater than our item? If so, discard the right half (shift the `end` variable to `midpoint - 1`).
    3. If the midpoint is less than our item, discard the left half (shift the `start` variable to `midpoint + 1`).
    4. Repeat the process until the item is found or the search space is empty.
  - Requires the collection to be **sorted**.
  - Can be implemented **iteratively** or **recursively**.
  
- **Considerations**:
  - Recursive signature is generally binary_search(array, low: int, high: int, item: T)
  - Sorting a collection has a cost, so when deciding whether to use binary search, consider the size of the collection (`n`) and the number of searches to perform. 
  - If `n` is small, the sorting cost may not be worth it. But for large `n` or frequent searches, sorting (a one-time operation) may make binary search more efficient.
  
- **Recursion Tip**:
  - If you use recursion and pass list slices (instead of indices), it may affect performance since slicing a list is O(k). To achieve true O(log n) performance, pass the indices to the recursive function instead.
