# Name: Teng Tze Hui & Ng Jace Xin
# Student ID: 2214209 & 2214593
# Class: DAA/2B/01

# Import
class Sort:

    # Initialize the steps attribute
    def __init__(self):
        self.steps = 0

    # Bubble Sort Function (implementation)
    def bubbleSort(self, l):
        self.steps = 0  # Reset steps for each sorting operation
        isSorted = False
        
        while not isSorted:
            isSorted = True
            for i in range(len(l)-1): # represents one pass of swapping.
                self.steps += 1  # Increment steps for each comparison
                if l[i]>l[i+1]:
                    l[i],l[i+1] = l[i+1],l[i]
                    isSorted = False 

    # Merge Sort Function (implementation)
    def mergeSort(self, l):
        self.steps = 0  # Reset steps for each sorting operation
        if len(l) > 1:
            mid = int (len(l)/2)
            
            # Here is where we split into two halves.
            leftHalf = l[:mid]
            rightHalf = l[mid:]
            
            # Recursive call 
            Sort.mergeSort(self, leftHalf)
            Sort.mergeSort(self, rightHalf)

            leftIndex,rightIndex,mergeIndex = 0,0,0
            
            # take cares of the merging 
            mergeList = l
            while leftIndex < len(leftHalf) and rightIndex < len(rightHalf):
                self.steps += 1  # Increment steps for each comparison

                if leftHalf[leftIndex] < rightHalf[rightIndex]:
                    mergeList[mergeIndex] = leftHalf[leftIndex]
                    leftIndex+=1
                else:
                    mergeList[mergeIndex] = rightHalf[rightIndex]
                    rightIndex+=1
                mergeIndex+=1

            # Handle those items still left in the left Half
            while leftIndex < len(leftHalf):
                mergeList[mergeIndex] = leftHalf[leftIndex]
                leftIndex+=1
                mergeIndex+=1

            # Handle those items still left in the right Half
            while rightIndex < len(rightHalf):
                mergeList[mergeIndex] = rightHalf[rightIndex]
                rightIndex+=1
                mergeIndex+=1 