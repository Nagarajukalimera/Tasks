#1.calculate the sum of squares of number from 1 to 5 
#using for loop
sum=0
for i in range(1,6):
    result=i**2
    sum+=result
print(sum) 

#2.print a countdown from 5 to 1 using while loop
count=5
while count>0:
    print(count)
    count-=1

#4.sum of even numbers between 0 to 10 using for loop
sum=0
for i in range(0,11):
    if i%2==0:
        sum+=i
print(sum)   

#3.multiplication table
table=int(input("enter a table: "))
for i in range(0,1):
    for j in range(1,11):
        print(f"{table}*{j}={table*j}")

#5.sum of all numbers from  1 to given number
num=int(input("enter a number: "))
sum=0
for i in range(1,num):
    sum+=i
print(sum)  

#6.display numbers from a list
list=[1,2,3,4,(1,2,3,4,),"list"]
for i in list:
    print(i)

#7.display numbers from -10 to -1
for i in range(-10,0):
    print(i)

#8.display prime numbers with in a range
num_1=int(input("enter a starting num in range: "))
num_2=int(input("enter a ending number in range: "))
for num in range(num_1,num_2):
    if num>1:
        for i in range(2,num):
            if num%1==0:
                break
        else:
            print(num)