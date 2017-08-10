# start_chat function definition

def start_chat():
    show_menu=True
    while show_menu:
        menu_choices=" What you want to do ? \n 1.Add Status \n 2.Close Application"
        result=int(raw_input(menu_choices))
        #validating user's input
        if(result==1):
            #action
            pass
        elif(result==2):
            show_menu=False
        else:
            print " Wrong Choices "