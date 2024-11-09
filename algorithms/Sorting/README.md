# Sorting Algorithms in Python

## Overview

Sorting generally refers to the process of comparing the elements of a collection, typically two at a time, and exchanging them if necessary based on a predetermined order (ascending or descending).

There are many sorting algorithms, and it's important to note that, just like searching algorithms, there is no "one size fits all" solution. In some cases, a complex sorting algorithm may not be worth the overhead for a small collection, and a simple sorting algorithm may not be efficient for a larger collection.

### Sorting Efficiency
Efficiency is generally measured in two ways:
- **Number of comparisons** made between elements.
- **Number of exchanges/swaps** made to reorder elements.

In this document, we'll explore various sorting algorithms, each utilizing different numbers of comparisons and exchanges, depending on the collection to be sorted.

### Swapping in Python vs Other Languages
In most programming languages, swapping two elements requires the use of a temporary variable:

```
a = "foo"
b = "bar"
# Swap using a temporary variable
temp = a
a = b
b = temp
```
In Python, however, we can do this more succinctly with tuple unpacking:
```
a, b = b, a
```

### Sorting Algorithms

## 1. Bubble Sort

Bubble Sort makes multiple passes through the list. It compares adjacent items and swaps them if the current item is larger than the next item. This process continues for n-1 passes, where n is the number of elements in the list.
- Time complexity: O(n²)
- Key characteristics:
    - Compares and swaps adjacent elements
    - First pass makes n-1 comparisons, second pass makes n-2, and so on.
    - Often regarded as the most inefficient sorting method due to high swap count.

## 2. Selection Sort

Selection Sort performs fewer swaps than Bubble Sort. It makes n-1 passes but swaps only once per pass by finding the next highest (or lowest) element and placing it in the correct position.
- Time Complexity: O(n²)
- Key Characteristics:
    - Makes the same number of comparisons as Bubble Sort but far fewer swaps.
    - Finds the maximum/minimum element in each pass and places it in the correct position.

## 3. Insertion Sort

Insertion Sort builds a sorted sublist one element at a time. Each new element is compared to items in the sorted sublist and inserted into the correct position. Unlike Bubble and Selection Sort, it shifts elements rather than swapping them.
- Time Complexity: O(n²)
- Key Characteristics:
    - Efficient for small data sets.
    - Less expensive in terms of processing power due to shifting rather than swapping.

## 4. Shell Sort

Shell Sort is an improvement over Insertion Sort. It breaks the list into multiple sublists, which are then sorted independently. These sublists are determined by a gap value, which reduces over time, eventually leading to an insertion sort on a nearly sorted list.
- Time Complexity: O(n²) in the worst case, but can perform better with specific gap sequences.
- Key Characteristics:
    - Reduces the amount of shifting required by insertion sort.
    - Efficient for larger data sets due to initial sublist sorting.

# 5. Merge Sort

Merge sort is a recursive divide and conquer sorting algorithm. The base case for recursion is a list with 1 element or no elements. This is also a sorted list, by definition. The idea is recursively splitting the list until the base case is reached. Then, the 'merge' happens. Where each sublist is compared and merged together in order.
- Time Complexity: O(n log n)
- Key Characteristics:
    - 

# 6. Quick Sort

Quick sort also approaches sorting with the divide and conquer approach, without added storage. However, if a list is not divided in half, performance is diminished. 

Quick sort makes use of a 'pivot value', there is lots of ways to choose this value, but for the sake of an example, I went with the first element in the example code. The purpose of the pivot value is to help split the list. You create two pointers... left and right mark. We increment left mark until we find a value bigger than 'pivot value' and we decrement right mark until we find a value less than 'pivot value. Then exchange these two values. Then repeat the process. Once the right mark becomes less than the left mark, we can swap the right mark with the pivot value. Pivot value is now in the correct place. 

The list can now be split at this split point, and quick sort can be done recursively on the left & right halves.

- Time complexity: O(n log n)
- Key characteristics:
    - Same time complexity as merge sort but requires less memory.
    - Can be more inefficient if the split points are not exactly in the middle and skewed to the side.
    - In these cases, quick sort is O(n²)
