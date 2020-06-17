S1='python is easy than java'
S2=S1.split(" ")
print('Before',S2)
temp=S2[0]
S2[0]=S2[len(S2)-1]
S2[len(S2)-1]=temp
print('After',S2)
//print('After',S2)
