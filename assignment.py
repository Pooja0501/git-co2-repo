while True:
    print("1.Add")
    print("2.Sub")
    print("3.multiplty")
    print("4.Division")
    print("5.Exit")
    choice=input('enter choice: ')
    if choice=='5':
            print("exiting calculator")
            break      
    if choice in ['1','2','3','4']:          
        num1=int(input("enter first number:"))
        num2=int(input("enter second number:"))
        if choice=='1':
            add=num1+num2
            print("addition is",add)
        elif choice=='2':
            sub=num1-num2
            print("subtraction is ",sub)
        elif choice=='3':
            mul=num1*num2
            print("multiplication is ",mul)
        elif choice=='4':
            if num2!=0:
                div=num1/num2
                print("division is ",div)
            else:
                print("invalid division")       
    else:
        print("invalid choice")
