print("Welcome to the Tip Calculator!")
totalBill=int(input("What was the Total Bill?"))
tipPerc=int(input("How much tip would you like to give? in percentage..."))
People=int(input("How many people to split the bill?"))

finalAmount= ((totalBill/100)*tipPerc)/People + totalBill

print("Each person should pay Rs.",finalAmount)