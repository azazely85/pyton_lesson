#square
type = input()
if(type=="треугольник"):
    a = float(input())
    b = float(input())
    c = float(input())
    p=(a+b+c)/2
    print((p*(p-a)*(p-b)*(p-c))**0.5)
elif(type=="прямоугольник"):
    a = float(input())
    b = float(input())
    print(a*b)
elif(type=="круг"):
    r=float(input())
    print(3.14*(r**2))
