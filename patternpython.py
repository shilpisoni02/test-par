string= input("enter the string")
length= len(string) #lenth of input = no of rows
for row in range(length): # length in the sense 0 to 5
    for col in range(row+1): # at row 0 i want 1 col,row=1 col=2,row=2 col=3
         print(string[col],end=" ")
    print() # for printing next line



