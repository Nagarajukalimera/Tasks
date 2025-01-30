#Task 1: Reverse List: Write Python code to reverse the order of elements in the given list my_list .Print the reversed list.

my_list = [10, 20, 30, 40, 50, 11]
my_list.reverse() # Reverse method used to reverse the elements of a list in place
print(my_list)

#Task 2:Common Elements:Given two lists list1 and list2 , find and print the common elements between them.

list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]

common_list = [i for i in list1  if i in list2] # adds common numbers by comparing if same number is on list2
print(common_list)

#Task 3:Unique Elements:Create a new list unique_list containing only the unique elements from the given list original_list . Print the unique list.

original_list = [1, 2, 2, 3, 4, 4, 5]

unique_list = list(set(original_list)) # converting llist removes duplicates
print(unique_list)

#Task 4:Remove Duplicates:Remove duplicate elements from the given list duplicated_list and print the list without duplicates while preserving the order.

duplicated_list = [1, 2, 2, 3, 4, 4, 5]

remove_depl = []


for i in duplicated_list:
    if i not in remove_depl: #checks if number not in empty list created
        remove_depl.append(i) # Then appends 
print(remove_depl)

#Exercise 1: List Concatenation Write a Python script that concatenates two lists and prints the result.

list_1 = [1,2,3,4,5,6,7,8]
list_2 = [9,10,11,12,13,14,15]

concat_list = list_1 + list_2 # concatinating lists
print(concat_list)

#Exercise 2: List Repetition Write a Python script that repeats a list three times and prints the result.

list_repeat = [12,14,"Bharath", 9.02]

print(3*list_repeat) # prints list 3 times

# Exercise 3: List Removal Write a Python script that removes the elements at even indices from a list.

list_remove = [1,2,3,4,5,6,7,8,9,10]
result = list_remove[::2] # Starts and 1 ends at end of list, skips even incide by adding 2
print(result)

#Exercise 4: List Insertion Quiz Questions: 4 Write a Python script that inserts the numbers 10, 11, and 12 at the beginning of a list
list_insert = [1,2,3,5,7,8]
list_insert.insert(0,10)
list_insert.insert(1,11)
list_insert.insert(2,12)
print(list_insert)

#List comprehensions : 
# #1. Square Numbers: Create a list of squares of numbers from 1 to 10.

list_squares = [i**2  for i in range(1,11)] # performs square for each number in list
print(list_squares)


#2. Even Numbers: Generate a list of even numbers from 1 to 20.

even_list = [i for i in range(1,21) if i%2==0]
print(even_list)

#3. Words Lengths: Given a list of words, create a list containing the lengths of each word.


words = ["apple", "banana", "cherry", "date"]

words_length = [len(word) for word in(words) ]
print (words_length)