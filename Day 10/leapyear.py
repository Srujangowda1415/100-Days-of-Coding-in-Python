def leap_year():
    leap=()
    year=int(input("Enter the Year here: "))
    if year%4==0:
        leap=True
        if year%100==0:
            leap=False
            if year%400==0:
                leap=True
            elif year%400!=0:
                 leap=False
                 
            
        else:
             leap=True
             
        
        
    else:
        leap=False

    return leap
print(leap_year())