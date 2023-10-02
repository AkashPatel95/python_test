list1=[5,20,15,20,25,50,20]
value_to_remove=int(input("enter a value to remove from list:"))

new_list=[]
for i in list1:
    if value_to_remove!=i:
        new_list.append(i)

print(new_list)
