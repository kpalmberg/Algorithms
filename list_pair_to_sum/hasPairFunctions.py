#Function to determine is a pair exists in the SORTED list which adds to the sum
#Linear time: O(n)
def pairExistsWithSum_SortedList(sortedList, sum):
    low = 0
    high = len(sortedList) - 1

    while low < high:
        currentPairSum = sortedList[low] + sortedList[high]
        if currentPairSum == sum:
            return True
        elif currentPairSum < sum:
            low += 1
        elif currentPairSum > sum:
            high -= 1
    return False

#Function to determine is a pair exists in the unsorted/sorted  list which adds to the sum
#This method is cleaner code & can deal with an unsorted list as opposed to SortedList method
#Linear time: O(n)
def pairExistsWithSum_unsortedOrSortedList(L1, sum):
    compliment = []
    for item in L1:
        if item in compliment:
            return True
        compliment.append(sum - item)
    return False

if __name__ == '__main__':
    L0 = [1, 4, 6, 2, 8]  # true expectation
    sum = 12

    print("Entering list L0")
    print(pairExistsWithSum_SortedList(L0, sum), "\n")