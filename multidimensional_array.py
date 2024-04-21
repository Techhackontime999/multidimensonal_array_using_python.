m=int(input("Enter number of rows :  "))
n=int(input("Enter nuber of column:  "))
o=[ ]
for i in range(m):
    l=[ ]
    for j in range(n):
        k=int(input(f"Enter a[{i}][{j}] element : "))
        l.append(k)
    o.append(l)    
print(f'''your array is {m}-dimensional
***********************************************''')    
print("Array is : \n",o)