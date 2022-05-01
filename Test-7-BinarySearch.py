import sys
sys.setrecursionlimit(10000)

def binary_search(array, value, low, high):
    if high < low:
        return -1
    else:
        mid = round((low + high)/2)
        if array[mid] > value:
            return binary_search(array, value, low, mid)
        elif array[mid] < value:
            return binary_search(array, value, mid+1, high)
        else:
            return mid


array = []
for i in range(10000):
    array.append(input())
for i in range(10000):
    value = input()
    answer = binary_search(array, value, 0, 9999)
    print("%d" % answer)



# for i in range(5):
#     array.append(input())
# for i in range(5):
#     value = input()
#     answer = binary_search(array, value, 0, 4)
#     print("%d" % answer)