a=float(input())
b=float(input())
c=float(input())
if a==b==c:
    print("tam giac Deu")
elif a==b or a==c or b==c:
    print("tam giac Can")
elif a**2+b**2==c**2 or a**2+c**2==b**2 or b**2+c**2==a**2:
    print("tam giac Vuong")
else:
    print("tam giac Thuong")
