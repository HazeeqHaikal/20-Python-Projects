def binarySearch(list, element):
    mid = 0 
    start = 0
    end = len(list)
    steps = 0
    
    while start <= end:
        print("Step", steps, ":", str(list[start:end + 1]))
        
        steps += 1
        mid = (mid + end) // 2
        
        if element == list[mid]:
            return mid
        elif element < list[mid]:
            end = mid - 1
        else:
            start = mid + 1
        
    return -1

myList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 10

binarySearch(myList, target)