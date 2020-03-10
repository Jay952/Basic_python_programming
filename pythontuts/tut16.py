list1=[ ["Jay",1],["Ajay",1],["Vijay",3],["Amar",4]]
print(list1)
dict1=dict(list1)
for  item,lollypop in dict1.items():
    print(item,lollypop)
print(dict1)


for item in dict1:
 print(item)

 list2=[1,2,4,5,7,8,9,"Ajay","Vijay","Jay"]
 for item in list2:
     if str(item).isnumeric() and item>=6:
         print(item)
         

