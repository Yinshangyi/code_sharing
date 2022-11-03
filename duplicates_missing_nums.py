from typing import List


def getDuplicateAndMissingValue(array: List[int]) -> int:
    """
     Solution:
     Create an array filled with 0 of size N
     [1, 2, 2, 4, 5]
     [0, 0, 0, 0, 0]
     Loop over the input array and Increment +1 the 0-filled array at each index such as:
     If array[0] = 1 => [1, 0, 0, 0, 0]
     If array[1] = 2 and array[3] = 2 => [1, 2, 0, 0, 0]
     For the input array [1, 2, 3, 4, 4, 6] => [1, 1, 1, 2, 0, 1]
     Each value in the array correspond to the number of occurrence of values in the input array
     Time complexity: O(N)
     Space complexity: O(N)
    """
    duplicateNum = 0
    missingNum = 0
    numCount = [0] * len(array)
    for num in array:
        indexToIncrement = num - 1
        numCount[indexToIncrement] += 1
    for index, count in enumerate(numCount):
        if count == 0:
            missingNum = index + 1
        if count > 1:
            duplicateNum = index + 1
    return {"missing": missingNum, "duplicate": duplicateNum}


def unitTest(arrayInput: List[int], expectedNumbers: dict):
    numbers = getDuplicateAndMissingValue(arrayInput)
    if numbers == expectedNumbers:
        print("ok")
    else:
        print("ko")
        print(str(numbers) + " != " + str(expectedNumbers))


unitTest(arrayInput=[1, 2, 3, 4, 4, 6], expectedNumbers={"missing": 5, "duplicate": 4})
unitTest(arrayInput=[1, 6, 3, 4, 5, 6], expectedNumbers={"missing": 2, "duplicate": 6})
unitTest(arrayInput=[1, 2, 3, 4, 2, 6], expectedNumbers={"missing": 5, "duplicate": 2})


