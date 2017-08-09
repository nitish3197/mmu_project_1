print " Calculator "
a=raw_input(" Enter the first number : ")
if len(a)>0 :
    b=raw_input(" Enter the second number ")
    if len(b)>0 :
        print " Press 1 for addition "
        print " Press 2 for subtraction "
        print " Press 3 for multiplication "
        print " Press 4 for division "
        c=raw_input(" Enter the option : ")
        if c=="1" :
            d=float(a) + float(b)
            print d
        if c=="2" :
            d=float(a) - float(b)
            print d
        if c=="3" :
            d=float(a) * float(b)
            print d
        if c=="4" :
            d=float(a) / float(b)
            print d
