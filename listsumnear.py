list = [int(i) for i in input().split()]
s="";
for i in range(len(list)):
    if len(list)==1:
        s += str(list[i])
    elif i+1==len(list):
        s += str(list[i - 1] + list[0])
    else:
        s += str(list[i - 1] + list[i+1])+" "
print(s)