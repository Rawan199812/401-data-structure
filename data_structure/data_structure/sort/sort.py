def insertion_sort(arr):

    for i in range(1, len(arr)):
        current_value = arr[i]
        current_position = i

        while current_position > 0 and arr[current_position - 1] > current_value:
            arr[current_position] = arr[current_position -1]
            current_position = current_position - 1

        arr[current_position] = current_value 
    return arr

# arr = [8,4,23,42,16,15]
# insertion_sort(arr)
# for i in range(len(arr)):
#     print (arr[i])

if __name__ == "__main__":
    print(insertion_sort([8,4,23,42,16,15]))