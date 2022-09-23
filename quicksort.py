def quickSort(list):
    if len(list) <= 1:
        return list
    else:
        pivot = list.pop()
        less = []
        greater = []
        
        for element in list:
            if element < pivot:
                less.append(element)
            else:
                greater.append(element)
        
        return quickSort(less) + [pivot] + quickSort(greater)

list = [2, 3, 1, 5, 4, 6, 7, 9, 20]

print(quickSort(list))