import copy

def insertionSort(item_list : list):
    sorted_list = copy.deepcopy(item_list)

    for i in range(1, len(sorted_list)):
        for j in range(i, 0, -1):
            if sorted_list[j] < sorted_list[j-1]:
                sorted_list.insert(j-1, sorted_list.pop(j))

    return sorted_list

def selectionSort(item_list : list):
    sorted_list = copy.deepcopy(item_list)

    for i in range(0, len(sorted_list)-1):
        min_index = i
        for j in range(i+1, len(sorted_list)):
            if sorted_list[j] < sorted_list[min_index]:
                min_index = j

        if min_index != i:
            sorted_list.insert(i, sorted_list.pop(min_index))

    return sorted_list

def bubbleSort(item_list : list):
    sorted_list = copy.deepcopy(item_list)

    sort_occurred = True
    while sort_occurred:
        sort_occurred = False
        for i in range(1, len(sorted_list)):
            if sorted_list[i] < sorted_list[i-1]:
                sorted_list.insert(i-1, sorted_list.pop(i))
                sort_occurred = True

    return sorted_list

def mergeSort(item_list : list):
    if len(item_list) > 1:
        half = len(item_list) // 2

        sorted_list_1 = mergeSort(item_list[:half])
        sorted_list_2 = mergeSort(item_list[half:])

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
        sorted_list = item_list

    return sorted_list

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

    x = [i for i in range(10)]
    random.shuffle(x)

    print(x)
    print(insertionSort(x))
    print("-----------------")
    print(x)
    print(selectionSort(x))
    print("-----------------")
    print(x)
    print(bubbleSort(x))
    print("-----------------")
    print(x)
    print(mergeSort(x))
    print("-----------------")
    print(x)
    print(quickSort(x))
    print("-----------------")
    print(x)