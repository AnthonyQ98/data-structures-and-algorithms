The process of sorting is generally referring to as the comparing the elements of a collection, generally two elements at a time, and exchanging them if necessary, based on a pre-determined or desired order.

There is many sorting algorithms, and its important to note that, just like searching algorithms... there is no 'one size fits all' answer as the best. In some cases, a complex sorting algorithm may not be worth the overhead for a small collection, and a simple sorting algorithm may not be worth it for a larger collection.

Sorting efficiency is generally measured in two ways:
- The number of comparisons made.
- The number of exchanges made.

We will see some methods of sort, that utilise different numbers of comparisons and exchanges, for the same collection, to sort.

- Just as a general rule of thumb: in most languages, you would require a 'temporary' variable to conduct a swap of elements. Here is how 'most' languages would swap two variables:
  - a = "foo"
  - b = "bar"
  - c = a <- new temp variable to hold the value at 'a'
  - a = b
  - b = c

  - In Python, this is not the case. We can do something like a, b = b, a and this would swap the values of a and b at the same time in one statement.

# Bubble Sort

- Makes passes through a list. 
- Compares adjacent items and swaps them if the 'current' item is larger than the next item. 
- Next item then takes 'currents' place. And current compares with the next item.
- First pass takes n-1 comparisons to pass through the list.
- Second pass takes n-1 comparisons to pass through the list.
- Overall, sorting will take n-1 passes (not comparisons). 
- Time is O(n^2)
- Often regarded as the most inefficient sorting method.

# Selection Sort

- Whilst bubble sort compares every element with its adjacent element in each pass and can potentially exchange n-1 times in a given pass, selection sort makes 1 pass swap maximum for any given pass.
- How it does this is by iterating through a list, keeping track of the next highest element, and placing the element in the correct place at the end of the pass. 
- As it makes the same number of comparisons and passes, it is still O(n^2) - so the same as the bubble sort.
- However, it makes signifcantly less swaps. So performs better in benchmark tests.

# Insertion Sort

- Still O(n^2)
- Maintains a sublist. Each item larger than the curr element is shifted right until an element the same size or smaller is found, then the item is inserted.
- Faster than selection sort as it is SHIFTING items, rather than swapping - which is estimated to consume about 1/3 of the processing power.

# Shell Sort

- Similiar to insertion sort, but breaks the list into many sublists, rather than one sublist.
- Sublists are measured by 'the gap', which is just a number of elements separating the elements of a sublist.
- ie... for a list [4, 5, 1, 3, 9, 6], with a gap 2.. we get a sublist [4, 1, 9] and [5, 3, 6].
- sorting these sublists... we get [1, 4, 9] and [3, 5, 6]
- combined... it now looks like [1, 3, 4, 5, 9, 6]..
- interesting... it looks sorted... almost. 
- Now we do an insertion sort.. but with a lot less shifting as the sublists with the gap are already sorted.
- Well, how is it better than an insertion sort if its doing an insertion sort + more?
- Because there is less shifting by the time the insertion sort is called.
- Shell sort is O(n^2) in the worst case.