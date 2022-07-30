# TODO:
# Refactor mergeSort() to work in O(N) space.
# quickSort() is not yet in-place.

import copy

def insertionSort(item_list : list):
    for i in range(1, len(item_list)):
        for j in range(i, 0, -1):
            if item_list[j] < item_list[j-1]:
                item_list.insert(j-1, item_list.pop(j))

def selectionSort(item_list : list):
    for i in range(0, len(item_list)-1):
        min_index = i
        for j in range(i+1, len(item_list)):
            if item_list[j] < item_list[min_index]:
                min_index = j

        if min_index != i:
            item_list.insert(i, item_list.pop(min_index))

def bubbleSort(item_list : list):
    sort_occurred = True
    while sort_occurred:
        sort_occurred = False
        for i in range(1, len(item_list)):
            if item_list[i] < item_list[i-1]:
                item_list.insert(i-1, item_list.pop(i))
                sort_occurred = True

def mergeSort(item_list : list):
    def rMergeSort(sub_list : list):
        if len(sub_list) > 1:
            half = len(sub_list) // 2

            sorted_list_1 = rMergeSort(sub_list[:half])
            sorted_list_2 = rMergeSort(sub_list[half:])

            # sorted_list = merge(sorted_list_1, sorted_list_2)
            sorted_list = []
            while len(sorted_list_1) > 0 and len(sorted_list_2) > 0:
                if sorted_list_1[0] < sorted_list_2[0]:
                    sorted_list.append(sorted_list_1.pop(0))
                else:
                    sorted_list.append(sorted_list_2.pop(0))

            if len(sorted_list) > 0:
                sorted_list.extend(sorted_list_1)
            if len(sorted_list_2) > 0:
                sorted_list.extend(sorted_list_2)

        else:
            sorted_list = sub_list

        return sorted_list
    
    sorted_list = rMergeSort(item_list)
    item_list.clear()
    item_list.extend(sorted_list)

def quickSort(item_list : list):
    presort_list = copy.deepcopy(item_list)

    if len(presort_list) == 1:
        return presort_list

    pivot_index = len(presort_list) // 2
    ptr_index = 0
    
    while ptr_index < pivot_index:
        if presort_list[ptr_index] > presort_list[pivot_index]:
            presort_list.append(presort_list.pop(ptr_index))
            pivot_index -= 1
        else:
            ptr_index += 1

    ptr_index = pivot_index + 1
    while ptr_index < len(presort_list):
        if presort_list[ptr_index] < presort_list[pivot_index]:
            presort_list.insert(0, presort_list.pop(ptr_index))
            pivot_index += 1
        ptr_index += 1

    sorted_list = []
    if pivot_index > 0:
        sorted_list.extend(quickSort(presort_list[:pivot_index]))
    sorted_list.append(presort_list[pivot_index])
    if pivot_index < len(presort_list) - 1:
        sorted_list.extend(quickSort(presort_list[pivot_index+1:]))

    return sorted_list

if __name__ == "__main__":
    import random

    def genRandomList():
        x = [i for i in range(10)]
        print(x)
        random.shuffle(x)
        print(x)
        return x

    x = genRandomList()
    insertionSort(x)
    print(x)
    print("-----------------")
    x = genRandomList()
    selectionSort(x)
    print(x)
    print("-----------------")
    x = genRandomList()
    bubbleSort(x)
    print(x)
    print("-----------------")
    x = genRandomList()
    mergeSort(x)
    print(x)
    print("-----------------")
    x = genRandomList()
    print(quickSort(x))
    print("-----------------")
    print(x)