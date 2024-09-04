# lets make a love calc
# count the number of times letter in true comes in the couples name 
# count the number of times letter in love comes in the couples name
# print count2,count2

name1=input("Enter first name here  ")
name2=input("Enter second name here  ")
upperName1=name1.upper()
upperName2=name2.upper()
t1=["T","R","U","E"]
t2=["L","O","V","E"]
countt1=0
countt2=0
for i in upperName1:
    if i in t1:
        countt1+=1
for i in upperName2:
    if i in t1:
        countt1+=1
for i in upperName1:
    if i in t2:
        countt2+=1
for i in upperName2:
    if i in t2:
        countt2+=1
print(countt1,countt2)