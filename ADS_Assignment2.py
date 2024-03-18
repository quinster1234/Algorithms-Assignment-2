#Algorithms and Data Structures
#Assignment 2
#Quincy Chan 100894159
#March 16, 2024

#given an array, show merge sort and quick sort

#we import winsound to make a sound for each time there is a swap in merge sort only
import winsound

#plays a sound effect for the number of swaps made (5 swaps = 5 beeps)
def playSound():
    #make a beep sound with frequency 800 and duration 100 ms
    winsound.Beep(800, 100)

#merge sort function
def mergeSort(arr):
    #if length of the array is 1 or less, it is sorted
    if len(arr) <= 1:
        return arr

    #splits the array into half, forming a left and right half
    midPoint = len(arr) // 2  
    leftHalf = arr[:midPoint]
    rightHalf = arr[midPoint:]

    #prints the current step of spliting the array in half
    print("Split:", arr)  

    #sorts the values on the left and right halves
    leftHalf = mergeSort(leftHalf)
    rightHalf = mergeSort(rightHalf)

    #merge the two sorted halves
    return merge(leftHalf, rightHalf)

#merge function that makes sound effect for the number of swaps
def merge(left, right):
    mergedArray = []
    leftSide, rightSide = 0, 0
    #this will swap the values into its correct place
    while leftSide < len(left) and rightSide < len(right):
        if left[leftSide] < right[rightSide]:
            mergedArray.append(left[leftSide])
            leftSide += 1
        else:
            mergedArray.append(right[rightSide])
            rightSide += 1
            #call playSound function to play a sound effect for the swap
            playSound()

    mergedArray.extend(left[leftSide:])
    mergedArray.extend(right[rightSide:])
    
    #prints the step where a sort takes place
    print("Sort:", left, right, "->", mergedArray)
    
    return mergedArray

#quick sort function
def quickSort(arr, originalArray):
    #if the array has 1 or less elements, then it is sorted
    if len(arr) <= 1:
        return arr

    #we will choose the pivot to be the middle-most element
    pivotIndex = len(arr) // 2
    pivot = arr[pivotIndex]
    
    #for elements less than the pivot
    left = [x for x in arr if x < pivot]
    #for elements equal the pivot
    middle = [x for x in arr if x == pivot]
    #for elements greater than the pivot
    right = [x for x in arr if x > pivot]

    print("Pivot:", pivot)
    print("Left side:", left)
    print("Middle:", middle)
    print("Right side:", right)

    return quickSort(left, originalArray) + middle + quickSort(right, originalArray)

#function prompts the user to enter the elements for the array separated by spaces
def getInput():
    while True:
        try:
            array = input("Enter the elements of the array separated by spaces: ").split()
            array = [int(num) for num in array]
            return array
        #when user enters a non-int input, an error message will appear
        except ValueError:
            print("Error: Invalid integer")

#this is the main function
def main():
    #grabs the input array
    array = getInput()
    print("Initial array:", array)
    #this makes a copy of the original array entered by the user for later use
    originalArray = array.copy()
    
    #displays the merge sorted array
    print("\nMerge sort:")
    mergeSorted = mergeSort(array)
    print("Sorted array (Merge sort):", mergeSorted)
    
    #displays the middle-most element and the quick sorted array
    print("\nQuick sort with middle element as pivot:")
    quickSorted = quickSort(array, originalArray)
    print("Sorted array (Quick sort):", quickSorted)

#this calls the main function
main()
