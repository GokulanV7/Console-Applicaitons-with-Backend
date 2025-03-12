

def deposit():
    amount=float(input("Enter the amount : "))
    if amount<0:
        print('*************************')
        print('Enter the valid amount : ')
        print('*************************')
    return amount


def withdraw():
    withamout=float(input("Enter the amount : "))
    if withamout<0:
        print('*************************')
        print('Enter the valid amount')
        print('*************************')
    return withamout

def balance():
    print(balance1)

balance1=0
is_running=True

while is_running:
    print('*************************')
    print('Please select your Method')
    print('*************************')
    print('1.Deposit')
    print('2.WithDraw')
    print('3.Balance')
    print('4.Exit')
    print('*************************')

    choice=int(input())

    if choice==1:
        balance1+=deposit()
        print('*************************')
        print('Deposit Successfully')
        print('*************************')
    elif choice==2:
        withamout=withdraw()
        if withamout > balance1:
            print('********************************')
            print('You not have sufficient Balance')
            print('********************************')
        else:
            balance1-=withamout
            print('*************************')
            print('Successfully withdrawed')
            print('*************************')
    elif choice==3:
        print('$',balance1)
    elif choice==4:
        is_running=False
    else:
        print('*************************')
        print('Enter the Valid Input')
        print('*************************')
print('********************************')    
print('Thank you! For Visiting our Bank')
print('********************************')