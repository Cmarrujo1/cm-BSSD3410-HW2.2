# Code taken from
#https://www.geeksforgeeks.org/binary-search/
#accessed on: 8.22.24
# no attribution/ no license listed
# Python3 code to implement iterative Binary
# Search.


def binarySearch(arr, low, high, x):

    while low <= high:

        mid = low + (high - low) // 2


        if arr[mid] == x:
            return mid


        elif arr[mid] < x:
            low = mid + 1

        else:
            high = mid - 1


    return -1



if __name__ == '__main__':
    arr = [2, 3, 4, 10, 40]
    x = 10


    result = binarySearch(arr, 0, len(arr)-1, x)
    if result != -1:
        print("Element is present at index", result)
    else:
        print("Element is not present in array")