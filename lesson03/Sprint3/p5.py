#def sortList(list):
#
#   for i in range(1, len(list)):
#
#        j = i - 1
#
#        while j >= 0 and (list[j+1] < list[j]):
#
#            list[j+1], list[j] = list[j], list[j+1]
#            
#            j -= 1
#
#    return list

def mergeSort(arr):

    return mergeSortHelper(arr, 0, len(arr) - 1)

def mergeSortHelper(arr, s, e):
    if e - s + 1 <= 1:
        return arr
    
    m = (s + e) // 2

    mergeSortHelper(arr, s, m)
    mergeSortHelper(arr, m+1, e)
    merge(arr, s, m, e)

    return arr

def merge(arr, s, m, e):
    L = arr[s:m+1]
    R = arr[m+1: e + 1]

    i = 0
    j = 0
    k = s

    while i < len(L) and j < len(R):

        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1

        k += 1

    while i < len(L):
        arr[k] = L[i]
        i += 1
        k += 1

    while j < len(R):
        arr[k] = R[j]
        j += 1
        k += 1

list = ["f","o","r","t","n","i","t","e","b","a","l","l","s"]
print(mergeSort(list))
