#Creating an unsorted array and print to console for show
unsorted = [64, 25, 12, 22, 11]
print("Unsorted array is:", unsorted)

#For loop to iterate through unsorted array
for i in range(len(unsorted)):

    #Made an indicator set to false to know if the array is being sorted or not
    hasSwapped = False

    #For loop to iterate from left to right and switch places of
    #the values biggest numbers moved to the rightmost spots
    for j in range(0, len(unsorted)-i-1):
        #Check to see if left spot is bigger than right
        if unsorted[j] > unsorted[j+1]:
            #Switch left spot with right spot if left is bigger
            unsorted[j], unsorted[j+1] = unsorted[j+1], unsorted[j]
            #set hasSwapped to true to continue going through array
            hasSwapped = True
    
    #Checks to see if the array is still being sorted
    if (hasSwapped == False):
        break
            
print("Bubble Sorted array potentially is:",unsorted)