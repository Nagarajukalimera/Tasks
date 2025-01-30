#1 Vowel Checker
v_1=input("Enter the letter:")
if v_1 in ["a","e","i","o","u"]:
    print("The letter is vowel")
else:
    print("The letter is consonent")
#2 Age Group Classification
age=int(input("Enter the age:"))
if age<=12:
    print("The age group is child")
elif age>=13 and age<=17:
    print("The age group is teenager")
elif age>=18 and age<=64:
    print("The age group is adult")
else:
    print("Senior citizen")
#3 Number Classifier
num_1=int(input("Enter an integer:"))
if num_1>0:
    print("The number is positive")
elif num_1<0:
    print("The number is negative")
else:
    print("The number is 0")
#4 Leap Year Checker
Leap_1=int(input("'Enter the year:"))
if Leap_1%4==0 and Leap_1%100!=0 or Leap_1%400==0:
    print("It is a leap year")
else:
    print("It is not a leap year") 
#5 Calculator
Num_1=int(input("Enter the First Number:"))
Num_2=int(input("Enter the Second Number:"))
operator=input("Enter an operator (+, -, *, /): ")
if operator=='+':
    result=Num_1+Num_2
    print(f"The result is {result}")
elif operator=='-':
    result=Num_1-Num_2
    print(f"The result is {result}")
elif operator=='*':
    result=Num_1*Num_2
    print(f"The result is {result}")
elif operator=='%':
    result=Num_1%Num_2
    print(f"The result is {result}")
#6 Short Hand If
x=8
result="Even number" if x%2==0 else "odd number"
print(result)
#7 Discount Calculator
org_price = float(input("Enter the original price: "))
dis_per = float(input("Enter the discount percentage: "))
discount_amount = (dis_per / 100) * org_price
final_price = org_price - discount_amount
print(f"{final_price}")
#8 BMI Calculator:
weight = float(input("Enter your weight (in kilograms): "))
height = float(input("Enter your height (in meters): "))
bmi = weight / (height ** 2)
print(f"{bmi}")




     


    