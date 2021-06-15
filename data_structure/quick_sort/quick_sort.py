
# def quick_sort(arr, left, right):
#      if left < right:
#         position = partition(arr, left, right)
#         quick_sort(arr, left, position - 1)
#         quick_sort(arr, position + 1, right)


# def partition(arr, left, right):
#     pivot= arr[right]
#     low  = left - 1
#     for i in (range()):
#           if arr[i] <= pivot:
#             low+=1
#             Swap(arr, i, low)

#     Swap(arr, right, low + 1)
#     return low + 1


# def Swap(arr, i, low):
#     temp = 0
#     temp  = arr[i]
#     arr[i] =  arr[low]
#     arr[low] =  temp

# easier 
def quick_sort(sequence):
    length = len(sequence)
    if length <1 :
        return sequence
    else:
        pivot = sequence.pop()

        items_greater = []
        items_lower = []

        for item in sequence:
            if item > pivot:
                items_greater.append(item)

            else:
                items_lower.append(item)

    return quick_sort(items_lower) + [pivot] + quick_sort(items_greater)

print(quick_sort([8,4,23,42,16,15]))
