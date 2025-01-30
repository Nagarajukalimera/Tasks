balance = 100000
while True: 
    option=int(input("enter the 1 for credit,enter the 2 for debit,enter the 3 for balance,enter the 4 for pin generation,enter the 5 for exit:"))
    def credit():
        if option==1:
            inp=int(input("enter the amount to credit:"))
            global balance
            balance+=inp
            print("credit sucessfully")
    credit()

    def debit():
        if option==2:
            inp=int(input("enter the amount to debit:"))
            global balance        
            print("debit successfully")
            balance-=inp 
    debit()  

    def balance():
        if option==3:
            global balance
            print(balance)
    balance()

    def pin():
        if option==4:
           inp=input("enter a new pin :")
           print("pin generated sucessfully")
    pin() 
    if option==5:
        print("thank you for visting")
        break       