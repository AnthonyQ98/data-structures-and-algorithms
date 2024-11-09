import random

# Defines the main function for quick sort on a list
def quick_sort(a_list):
    # Calls the helper function with the list and boundary indices (first and last element)
    quick_sort_helper(a_list, 0, len(a_list) - 1)

# Helper function to perform recursive quick sort
def quick_sort_helper(a_list, first, last):
    # Only sort if the segment has more than one element
    if first < last:
        # Partition the list and get the split point
        split = partition(a_list, first, last)
        # Recursively quick sort the left part
        quick_sort_helper(a_list, first, split - 1)
        # Recursively quick sort the right part
        quick_sort_helper(a_list, split + 1, last)

# Function to partition the list and choose a pivot
def partition(a_list, first, last):
    # Selects the first element as the pivot
    pivot_val = a_list[first]
    # Initialize markers for elements to the left and right of the pivot
    left_mark = first + 1
    right_mark = last
    done = False  # Flag to control the while loop

    # Continue until markers cross
    while not done:
        # Move left marker to the right as long as elements are less than the pivot
        while left_mark <= right_mark and a_list[left_mark] <= pivot_val:
            left_mark = left_mark + 1
        # Move right marker to the left as long as elements are greater than the pivot
        while left_mark <= right_mark and a_list[right_mark] >= pivot_val:
            right_mark = right_mark - 1
        # If markers cross, exit the loop
        if right_mark < left_mark:
            done = True
        else:
            # Swap elements at the left and right markers
            a_list[left_mark], a_list[right_mark] = a_list[right_mark], a_list[left_mark]

    # Place the pivot in its correct position
    a_list[first], a_list[right_mark] = a_list[right_mark], a_list[first]

    # Return the position of the pivot
    return right_mark

# Main function to generate a random list, sort it, and print the result
def main():
    # Generate a list of 10,000 random integers between 0 and 10,000
    some_list = [random.randint(0, 10000) for _ in range(10000)]
    # Sort the list using quick_sort
    quick_sort(some_list)
    # Print the sorted list
    print(some_list)

# Check if this file is run directly (not imported)
if __name__ == "__main__":
    # Run the main function
    main()
