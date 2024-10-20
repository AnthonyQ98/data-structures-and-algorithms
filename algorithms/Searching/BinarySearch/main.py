def binary_search(_list, item):
    found = False
    last = len(_list) - 1
    first = 0

    while first <= last and not found:
        midpoint = (first+last) // 2
        if _list[midpoint] == item:
            found = True
        else:
            if item < _list[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1

    return found      

def binary_search_recursive(_list, item):
    if len(_list) == 0:
        return False
    else:
        midpoint = len(_list) // 2
        if _list[midpoint] == item:
            return True
        else:
            if item < _list[midpoint]:
                return binary_search_recursive(_list[:midpoint], item)
            else:
                return binary_search_recursive(_list[midpoint+1:], item)

    return False         


# PREFERRED METHOD - compare with the others to spot the differences
def binary_search_recursive_with_indices(_list, low, high, item):
    if high >= low:
        midpoint = (high+low) // 2

        if _list[midpoint] == item:
            return True
        
        elif _list[midpoint] > item:
            return binary_search_recursive_with_indices(_list, low, midpoint - 1, item)
        
        else:
            return binary_search_recursive_with_indices(_list, midpoint+1, high, item)
        
    else:
        return False

def main():
    sorted_list = [12, 24, 36, 48, 60, 72, 84, 96, 108, 120, 132, 144, 156, 168, 180]
    
    print(binary_search(sorted_list, 24))
    print(binary_search(sorted_list, 25))
    print(binary_search(sorted_list, -1))


    print(binary_search_recursive(sorted_list, 24))
    print(binary_search_recursive(sorted_list, 25))
    print(binary_search_recursive(sorted_list, -1))
    
    print(binary_search_recursive_with_indices(sorted_list, 0, len(sorted_list)-1, 24))
    print(binary_search_recursive_with_indices(sorted_list, 0, len(sorted_list)-1, 25))
    print(binary_search_recursive_with_indices(sorted_list, 0, len(sorted_list)-1, -1))

if __name__ == "__main__":
    main()