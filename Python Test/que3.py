list1=[10,20,30,40]
list2=[100,200,300,400]

for i in range(len(list1)):
    item1=list1[i]
    item2=list2[-i-1]
    print(item1,item2)
