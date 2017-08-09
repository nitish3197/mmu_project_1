# import statements
from spy_details import spy_name,spy_salutation,spy_age,spy_rating

print "Let's get started "
question="Do you want to continue as "+spy_salutation+" "+spy_name+" (Y/N) : g"
existing=raw_input(question)
# check vaidating user input
if (existing=="Y" or existing=="y") :
    pass
elif (existing =="N" or existing =="n") :
    spy_name=raw_input("Enter your name : ")
    if len(spy_name)>0 :
        if spy_name.isalpha():
            print "Alright "+spy_name+ " I would like to know better before you proceed.. "
            spy_salutation=raw_input(" Enter what should we call you : ")
            spy_name=spy_salutation+" "+spy_name
            print "Welcome "+ spy_name+" Glad to have you back with us."
            spy_rating=0
            spy_rating=0.0
            spy_online=False
            print type(spy_age)
            spy_age=int(raw_input(" Enter the age of spy "))
            if (type(spy_age)==int) :
                print " Valid age "
                if spy_age > 15 and spy_age < 50 :
                    spy_rating = bool(raw_input(" Enter the rating of the spy "))
                    print type(spy_rating)
                else :
                     print "Not valid age"
        else :
            print "Invalid Name "
    else:
        print "Invalid input"
else:
    print "wrong choice "









