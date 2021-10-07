# Group project 325 - SA sorting
def recursion(arr, target):
    countOfComparison = 0
    tempIndex = target

    for j in range(target+1, len(arr)):
        if (arr[tempIndex] > arr[j]):
            arr[j], arr[tempIndex] = arr[tempIndex], arr[j]
            tempIndex = j
            print(arr)
            countOfComparison += 1

    if (countOfComparison > 0):
        recursion(arr, target)

    else:
        return(arr)
                    

def sort(arr):
    target = 0

    #for i in range(len(arr)):
    for target in range(len(arr)):
        print("Target = {}".format(target))
        print(arr)
        recursion(arr, target)
        print("Done round....")
        #target += 1
      


arr = [5,6,3,9,4,8,1]

sort(arr)

print(arr)




