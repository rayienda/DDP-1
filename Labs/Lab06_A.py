# Rayienda Hasmaradana
# KKI

#selection_sort(): sorts a list in place, using selection sort algorithm recursively

def minIndex(lst, startIndex):
   # base case: only one element to consider
   if startIndex == len(lst)-1:
      return startIndex
   # Find minimum of remaining elements recursively
   k = minIndex(lst, startIndex + 1)
   # Return the minimum of all
   if lst[startIndex] < lst[k]:
      return startIndex
   else:
      return k
   
## selection_sort( ):
# sorts a list in place, using selection sort recursively.
# @param lst: the list to sort
# @param startIndex: the index of starting element
#

def selection_sort(lst, startIndex = 0):
 n = len(lst)
 # when starting index and size of list are the same, return; because there is nothing to sort

 if startIndex == len(lst): return
 # find the index of minimum element from startIndex to the end

 k = minIndex(lst, startIndex)
 # Swapping the corresponding elements when the found index and the current minimum index are not the same
 
 if k != startIndex:
    lst[k], lst[startIndex] = lst[startIndex], lst[k]
 # Recursively calling selection sort function for the remaining elements

 selection_sort(lst, startIndex + 1)

# main(): demonstrates the selection sort algorithm by sorting a list of integers given by user

def main():
   input_string = input("Type a sequence of numbers (example: 3,100,-5,3): \n") #taking input from user
   if input_string =='':
      values = [] # create empty list if the input is empty
   else:
      values = input_string.split(",") ## Splitting the input string into a list of strings based on comma delimiter

 # change each element from str to int
   for i in range(len(values)):
      values[i] = int(values[i])
   print('Input list:\n',values) # print the input taken from user

   selection_sort(values) #call the selection_sort function to sort the input list

   print('Sorted list:\n',values) #print the sorted input list from the user

# check if the script is being run directly
if __name__ == '__main__':
   main()