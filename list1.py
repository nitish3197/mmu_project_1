
list=["Apple","Banana","Mango","Orange"]
print list
x=int(raw_input(" Enter the index to view its value : "))
print list[x]
option=raw_input(" Want to add an element in the list.Enter Yes/NO : ")
if option=="Yes":
    a=raw_input(" Enter the element : ")
    list.insert(5,a)
    print list

