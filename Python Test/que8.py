str1 = "PYnative29@#8496"
total = 0
count = 0

for i in str1:
    if i.isdigit():  
        total += int(i)  
        count += 1

print("Total:",total)
print("Average:",total/count)


