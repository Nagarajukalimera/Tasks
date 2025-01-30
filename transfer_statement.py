#1.numbers=[25,30,20,40,15,25]
list=[25,30,20,40,15,25]
sum=0
for i in list:
    if sum>100:
        break
    sum+=i
print(f"{sum} is exceed the 100")

#2. 1to600 print odd numbers,skipping even numbers using continue statement
for i in range(1,601):
    if i%2==0:
        continue
    print(i)

#3. check even or odd using pass statement
#conditional statement:if
num=int(input("enter a num: "))
if num%2==0:
    print(f"{num} is even num")
else:
    pass

#4.write a python script that iterates through a list of words.if the word is break,exit the loop using the break statement 
#if the word is "skip",skip the rest of the code for the current iteration using continue statement 
list=["return","tuple","go","skip","continue","break"]
for i in list:
    if i=="break":
        break
    if i=="skip":
       continue
    print(i)

    