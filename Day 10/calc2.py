def add(n1,n2):
    result=n1+n2
    return result
def minus(n1,n2):
    result=n1-n2
    return result
def product(n1,n2):
    result=n1*n2
    return result
def divide(n1,n2):
    result=n1/n2
    return result

welcome_message="Hello User! Have a nice calculating experience"
operand_list=("+\n"
             "-\n"
             "*\n"
             "/\n")
print(welcome_message)
input1=int(input("Please enter the first number in integer form \n"))
float1=float(input1)
input2=int(input("Please enter the second number in integer form \n"))
float2=float(input2)
print(operand_list)
operand=input("Please input the operation:")
result=""
if operand=="+":
    print(add(float1,float2))
    
elif operand=="-":
    print(minus(float1,float2))

elif operand=="*":
    print(product(float1,float2))
    
elif operand=="/":
    print(divide(float1,float2))
else:
    print("You have entered an invalid input")
    

