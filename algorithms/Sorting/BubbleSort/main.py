def bubble_sort(_list):
    for i in range(len(_list) -1, 0, -1): # loop this number of times (passes), starting from len of list minus 1 (in this case... 10-1)... until i is 0. 10-1, 10-2, 10-3.. etc
        for j in range(i): # number of comparisons on this pass, will be 1 less each pass.
            if _list[j] > _list[j+1]: # swap scenario
                _list[j], _list[j+1] = _list[j+1], _list[j] # notice: single statement swapping python allows.

def bubble_sort_short(_list): # breaks from the func when the sort is completed, regardless of passes. Also called 'short bubble'
    for i in range(len(_list) -1, 0, -1): 
        for j in range(i): 
            exchanges = False
            if _list[j] > _list[j+1]: # swap scenario
                exchanges = True
                _list[j], _list[j+1] = _list[j+1], _list[j] 
            if not exchanges:
                break

def main():
    some_list = [10, 2, 1, 9, 4, 7, 4, 3, 19, 1]
    bubble_sort(some_list)
    print(some_list)
    
if __name__ == "__main__":
    main()