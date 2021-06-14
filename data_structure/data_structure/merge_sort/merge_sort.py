def merge_sort(arr):
    n = len(arr)
    # print(n,"len")

    if n > 1:
        mid = n//2
        left = arr[0:mid]
        right = arr[mid:n]
        # print(mid, "mid")
        # print(left, "left")
        # print(right, "right")
        merge_sort(left)
        merge_sort(right)

        i = 0
        j = 0
        k = 0
        while i < len(left) and j < len(right):
            print(i , "i", len(left),"len(left)", j,"j", len(right),"len(right)")
            if left[i] <= right[j]:
              arr[k] = left[i]
              i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1
        print(k,"k")
        
merge_sort([8,4,23,42,16,15])
