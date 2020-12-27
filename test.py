val_arr = []
mid_arr = []
lo_arr = []
hi_arr = []


def binary_search(array, query):
    lo, hi = 0, len(array) - 1
    while lo <= hi:
        lo_arr.append(lo)
        hi_arr.append(hi)
        # Calculate mid
        mid = (hi + lo) // 2
        mid_arr.append(mid)
        # get cal for mid
        val = array[mid]
        val_arr.append(mid)
        if val == query:
            return mid
        elif val < query:
            lo = mid + 1
        else:
            hi = mid - 1
    return None


arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

len(arr)

binary_search(arr, 2)

lo_arr
hi_arr
mid_arr
val_arr

