#Quiz and Coding Exercise

#Quiz:
# 1. What does the break statement do ?
# Ans.  b) Exits the loop immediately

#  2. When is the continue statement used ?
#Ans.  b) To skip the rest of the code for the current iteration and move to the next

#  3. What is the purpose of the pass statement ?
#b) Skips the current iteration of a loop 

#********************Coding Exercise***********************

'''
Problem 1: Using break in a While Loop
Write a Python program that takes a list of numbers as input 
numbers = [25, 30, 20, 40, 15, 25] and prints the sum of the numbers. However, if the sum exceeds 
100, stop adding numbers and print "Sum exceeded 100"
'''

sum=0
numbers_input = [25, 30, 20, 40, 15, 25]
for num in numbers_input:
    sum +=num
    if sum >=100:
        break
    print(sum)
print("Sum exceeded 100")

'''
Problem 2. Using continue in a For Loop
Write a Python script that uses a for loop to iterate through numbers from 1 to 
600. Print only the odd numbers, skipping the even ones using the continue statement
'''

for i in range(1, 601):
    if i%2 == 0:
        continue
    print(i)


'''Problem 3. Using pass in Conditional Statements
Write a Python script that checks if a number is even or odd. If the number is 
even, print "Even"; if odd, do nothing (use the pass statement).
'''

user_number = int(input("Enter the number :"))
if user_number %2 ==0:
    print (f"Your number is Even number : {user_number}")
pass


'''
Problem 4. Combining Transfer Statements
Write a Python script that iterates through a list of words. If the word is "break," 
exit the loop using the break statement. If the word is "skip," skip the rest of the 
code for the current iteration using the continue statement. For any other word, 
print the word.
'''
Your_Word = ["break","skip","continue","hello"]
for Your_Word in Your_Word :
    if Your_Word == "break":
        break
    elif Your_Word == 'skip':
        continue
else:
    print(Your_Word)

    

    
 