a = int(input())
b = int(input())
c = int(input())
d = int(input())
if a<=0 or b<=0 or c<=0 or d<=0:
    print ("No")
elif (a + b == c + d) or (a + c == b + d) or (a + d == b + c):
    print("Yes")
else:
    print("No")
