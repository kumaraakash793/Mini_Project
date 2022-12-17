print("----WELCOME TO ATM ABC BANK--- ")
print("PLEASE INSERT YOUR CARD ")
password=1234
balance=10000
choice=0
pin=int(input("enter your pin "))
if pin == password:
    while choice != 4:

        print(" /////--MENU--///")
        print(" 1 == Balance")
        print(" 2 == Deposite ")
        print(" 3 == Withdraw ")
        print(" 4 == Exit")
        choice=int(input("Enter You Option "))
        if choice ==1 :
            print(f"YOur Current Balance is {balance}")
        elif choice ==2 :
            amount=int(input("Enter amount :"))
            balance=balance+amount
            print(f"Your Balance is Rs{balance}")
        elif choice ==3 :
            amount=int(input("enter amount "))
            if amount<=balance:
                balance = balance - amount
                print(f"Your Remain Amount is {balance}")
            else :
                print(f"Your balance is low {balance}")
        elif choice == 4:
            break
else :
    print("INVALID PIN NUMBER")
print("--Thanks for Visiting--")
