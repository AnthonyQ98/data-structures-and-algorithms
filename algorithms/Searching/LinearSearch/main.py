def linear_search(_list, item):
    found = False
    pos = 0

    while pos < len(_list) and not found:
        if _list[pos] == item:
            found = True
        else:
            pos += 1
    return found

def linear_search_sorted(_list, item):
    
    found = False
    pos = 0
    stop = False

    while pos < len(_list) and not found and not stop:
        if _list[pos] == item:
            found = True
        else:
            if _list[pos] > item:
                stop = True
            else:
                pos += 1
    return found

def main():
    listOfItems = [1, 9, 130, 291, 202002, 201]
    print(linear_search(listOfItems, 130))
    print(linear_search(listOfItems, 0))

    listOfSortedItems = [1, 9, 130, 201, 291, 202002]

    print(linear_search_sorted(listOfSortedItems, 130)) # same efficiency as unsorted linear search
    print(linear_search_sorted(listOfSortedItems, 6)) # slightly more efficient finding elements not in array when sorted


if __name__ == "__main__":
    main()