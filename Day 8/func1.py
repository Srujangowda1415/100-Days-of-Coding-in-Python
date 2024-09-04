def yeMeraPehlaFunctionNahiHai(i):
    i+=1
    print(i)
    i-=1
    print(i)
    i=i*i
    print(i)

def loveCounter(name1,name2):
    firstName=(name1.upper()).split()
    secondName=(name2.upper()).split()
    t1=firstName.count("T")
    t2=firstName.count("R")
    t3=firstName.count("U")
    t4=firstName.count("E")
    t5=secondName.count("T")
    t6=secondName.count("R")
    t7=secondName.count("U")
    t8=secondName.count("E")
    print(t1+t2+t3+t4+t5+t6+t7+t8)

loveCounter("abhay","kumar")
