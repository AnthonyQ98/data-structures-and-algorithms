def selection_sort(a_list):
    for i in range(len(a_list)):
        min_idx = len(a_list) - 1
        for j in range(i, len(a_list)):
            if a_list[j] < a_list[min_idx]:
                min_idx = j
        if min_idx != i:
            a_list[min_idx], a_list[i] = a_list[i], a_list[min_idx]

def main():
    some_list = [10, 2, 1, 9, 4, 7, 4, 3, 19, 1]
    selection_sort(some_list)
    print(some_list)
    
if __name__ == "__main__":
    main()