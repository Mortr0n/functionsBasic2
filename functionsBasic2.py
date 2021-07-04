# 1. Countdown - Create a function that accepts a number as an input. 
# Return a new list that counts down by one, from the number 
# (as the 0th element) down to 0 (as the last element).
# Example: countdown(5) should return [5,4,3,2,1,0]
# numList=[]
# def countdown(num):
#     for x in range(num, -1, -1):
#         numList.append(x)
#     return numList
# print(countdown(14))

# 2. Print and Return - Create a function that will receive a list with two numbers. 
# Print the first value and return the second.
# Example: print_and_return([1,2]) should print 1 and return 2

# def printReturn(a,b):
#     print(a)
#     return(b)
# print(printReturn(4,5))
# print(printReturn(-40,95))
# print(printReturn(0,8) + printReturn(8,8))

# 3. First Plus Length - Create a function that accepts a list and returns 
# the sum of the first value in the list plus the list's length.
#Example: first_plus_length([1,2,3,4,5]) should return 6 (first value: 1 + length: 5)

# def firstPlusLength(someList):
#     return someList[0]+len(someList)

# print(firstPlusLength([1,2,3,4,5,10,15]))

# 4. Values Greater than Second - Write a function that accepts a list 
# and creates a new list containing only the values from the original 
# list that are greater than its 2nd value. Print how many values this is 
# and then return the new list. If the list has less than 2 elements, have the 
# function return False
# Example: values_greater_than_second([5,2,3,2,1,4]) should print 3 and return [5,3,4]
# Example: values_greater_than_second([3]) should return False

# def valuesGreaterthanSecond(numList):
    
#     newList = []
#     if(len(numList)>2):
#         second = numList[1]
#         for num in range(0, len(numList), 1):
#             if(numList[num]>second):          
#                 newList.append(numList[num])
#         print(len(newList))
#         return newList
#     else:
#         return False

# print(valuesGreaterthanSecond([5,2,3,2,1,4]))
# print(valuesGreaterthanSecond([3]))
# print(valuesGreaterthanSecond([52,-2,3,2,1,4,-1,0,-3,-5]))

# 5. This Length, That Value - Write a function that accepts two integers 
# as parameters: size and value. The function should create and return a 
# list whose length is equal to the given size, and whose values are all 
# the given value.
# Example: length_and_value(4,7) should return [7,7,7,7]
# Example: length_and_value(6,2) should return [2,2,2,2,2,2]

# def thisLengthThatValue(size, value):
#     newList = []
#     for x in range(size):
#         newList.append(value)
#     return newList
# print(thisLengthThatValue(4,7))
# print(thisLengthThatValue(6,2))
# print(thisLengthThatValue(0,3))