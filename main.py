print " Let's get started !!!! "
spy_salutation = raw_input("Enter what should we call you : ")
if len(spy_salutation)>0:
    spy_name = raw_input(" Enter your name : ")
    if len(spy_name)>0:
        spy_name = spy_salutation + " " + spy_name
        print " Hello "+ spy_name + " !! We are glad to have you back with us. "


