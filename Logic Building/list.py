# Given a list, write a Python program to swap first and last element of the list.
# Input : [12, 35, 9, 56, 24]
# Output : [24, 35, 9, 56, 12]

# Input : [1, 2, 3]
# Output : [3, 2, 1]

def swapList(newList):
    size = len(newList)
    temp = newList[0]
    newList[0] = newList[size-1]
    newList[size-1] = temp

    return newList

newList = [24, 35, 9, 56, 12]
print(swapList(newList))


def swapList1(newList1):
    # temp = newList[0]
    # newList[0] = newList[-1]
    # newList[-1] = temp
    newList1[0], newList1[-1] = newList1[-1], newList1[0]

    return newList1

newList1 = [34,45,65,77,89,90]
print(swapList1(newList1))