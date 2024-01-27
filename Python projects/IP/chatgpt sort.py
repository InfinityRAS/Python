def bubble_sort(input_list):
    n = len(input_list)

    # Traverse through all elements in the list
    for i in range(n):
        print("in loop1")
        # Last i elements are already in place, so we don't need to check them
        for j in range(0, n - i - 1):
            print("in loop2")
            # Swap if the element found is greater than the next element
            if input_list[j] > input_list[j + 1]:
                input_list[j], input_list[j + 1] = input_list[j + 1], input_list[j]

# Example usage:
my_list = [4, 2, 7, 1, 9, 5]
bubble_sort(my_list)
print(my_list)
