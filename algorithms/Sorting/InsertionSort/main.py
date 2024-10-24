def insertion_sort(a_list):
    for i in range(1, len(a_list)): # important: starts at index 1 (not 0), as the sublist of 1 element is already considered sorted, so we can skip to the 2nd element (1 index)
        cur_val = a_list[i]
        cur_pos = i

        while cur_pos > 0 and a_list[cur_pos - 1] > cur_val:
            a_list[cur_pos] = a_list[cur_pos - 1]
            cur_pos = cur_pos - 1
        a_list[cur_pos] = cur_val

def main():
    some_list = [10, 2, 1, 9, 4, 7, 4, 3, 19, 1]
    insertion_sort(some_list)
    print(some_list)
    
if __name__ == "__main__":
    main()