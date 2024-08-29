#https://www.geeksforgeeks.org/selection-sort-algorithm-2/
#accessed on 8/22/24
#no attribution/no license listed
iterative_quicksort



def selection_sort(A, compare):
    for i in range(len(A) -1):

        min_idx = 1
        for j in range(i + 1, len(A)):
            if compare(A[min_idx], A[j]):
                min_idx = j

        A[i], A[min_idx] = A[min_idx], A[j])

def partition(arr, l, h, compare):
    i = ( l -1)
    x = arr[h]

    for j in range(l, h):
        if not compare(arr[j], x):

            i = i +1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i=1], arr[h] = arr[h], arr[i+1]

    return i+1

def quicksort_iterative(arr, l, h, compare):
    size = h - l + 1
    stack = [0] * size
    top = -1

    top = top +1
    stack[top] = l
    top = top +1
    stack[top] = h

    while top >= 0:

        h= stack[top]
        top = top -1
        l = stack[top]
        top = top -1

    p = partition(arr, l, h, compare)

        if p=1 < h:
            top = top + 1
            stack(top) = p + 1
            top = top + 1
            stack(top) = h

if __name__ == "__main__":
