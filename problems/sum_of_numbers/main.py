def list_sum_recursive(num_list):
    if len(num_list) == 0:
        return 0
    if len(num_list) == 1:
        return num_list[0]
    else:
        return num_list[0] + list_sum_recursive(num_list[1:])

def list_sum_iterative(num_list):
    _sum = 0
    for num in num_list:
        _sum += num
    return _sum


def main():
    list_of_numbers = [10, 20, 30, 5, 2]
    print(list_sum_recursive(list_of_numbers))
    print(list_sum_iterative(list_of_numbers))

    list_of_numbers = []
    print(list_sum_recursive(list_of_numbers))
    print(list_sum_iterative(list_of_numbers))

if __name__ == "__main__":
    main()