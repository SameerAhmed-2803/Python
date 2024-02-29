#Trying to relearn the sorting algorithms

#Creating an unsorted array and print to console for show
unsortedArray = [64, 25, 12, 22, 11]
print("Unsorted array is:", unsortedArray)

#For loop to iterate through the length of the array 
for i in range(len(unsortedArray)):
    #set the min number to value of i
    minNum = i
    #2nd 'for loop' to iterate through the remaining array to see 
    #if a number is smaller then current min
    for j in range(i+1, len(unsortedArray)):
        if unsortedArray[j] < unsortedArray[minNum]:
            minNum = j

    #Swaps the min number to the first position of array        
    unsortedArray[i], unsortedArray[minNum] = unsortedArray[minNum], unsortedArray[i]

print("Selection Sorted array is:", unsortedArray)
    