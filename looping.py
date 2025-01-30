# sum of squares
'''
sum=0
for i in range(1,6):
  result=i*2
  sum+=result
  print(sum)

# reverse count down
count=5
while count>0:
  print(count)
  count-=1
  
# multiplication table using nested for
first_num=int(input("enter the first number:"))
last_num=int(input("enter the last number:"))
for i in range(first_num,last_num+1):
    for j in range(1,11):
        print(f"{i}*{j}={i*j}")
        print()

# sum of even numbers
sum=0
for i in range (0,11):
    if i%2==0:
        sum+=i
    print(f"the sum of all even numbers between 0 and 10 is:",sum)

# sum of all numbers
num=int(input('enter a number'))
sum_of_num=num*(num+1)//2
for i in range(1,num+1):
    print(f" the sum of all numbers from 1 to num is", sum_of_num)

# display number in list
list=[1,2,3,4,3,5,4,7,34,54,6,3,7,4]
for i in list:
    print(i)

# display numbers from -10 to -1
for i in range(-10,0):
    print(i)
'''
# write a prime numbers
first_number=int(input("enter the first number:"))
last_number=int(input("enter the last number:"))
for num in range(first_number,last_number+1):
    if num>1:
        for i in range(2,num):
            if num%i==0:
                break
            else:
                print(num)

# write a prime number
first_number=int(input("enter the first number:"))
last_number=int(input("enter the last number:"))
for i in range(first_number,last_number+1):
    for j in range(2,i):
        print(i)
        if i%j==0:
            break
    else:
        print(i)
              

