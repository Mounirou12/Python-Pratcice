def sum_array(arr):
    #your code here
    if arr== None or  len(arr) <3 :
        return 0
    arr.remove(max(arr))
    arr.remove(min(arr))
    return sum(arr)
#   return sum(arr) - max(arr) - min(arr)


print(sum_array([6, 2, 1, 8, 10]))

print(sum_array([1, 1, 11, 2, 3]))

print(sum_array([]))

print(sum_array([3]))

print(sum_array(None))

