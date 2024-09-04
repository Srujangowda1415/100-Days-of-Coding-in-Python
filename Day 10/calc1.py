print("Hello User! Have a nice experience calculating...")

first_number=int(input("Please input the first number"))
should_continue=True
result=""
float1=float(first_number)
while should_continue:
    print(" + \n"
        " - \n"
        " * \n"
        " / \n")
    operation=input("Choose your operation")
    second_number=int(input("Please input the second number"))
    
    float2=float(second_number)

    if operation=="+":
        result=float1+float2
    elif operation=="-":
        result=float1-float2
    elif operation=="*":
        result=float1*float2
    elif operation=="/":
        result=float1/float2
    else:
        print("Invalid input datatype")
    print(f"Your result is: {result}")
    y=input("Do you wish to continue further?\n"
            "input 'end' to exit \n"
            "input 'y' to continue calculating with the same result \n"
            "input 'n' to proceed with a new calculation\n").upper()
    float1=result
    if y=="END":
        print("Thank you for visiting here! See you soon...")
        should_continue=False
    elif y=="Y":
        float1=result
    elif y=="N":
        first_number=int(input("first number"))
        float1=float(first_number)


        
