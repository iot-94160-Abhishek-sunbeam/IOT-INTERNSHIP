import calculator as c
a=int(input("enter the first number = "))
b=int(input("enter the second number = "))

print(f"{a}+{b}={c.add(a,b)}")
print(f"{a}-{b}={c.sub(a,b)}")
print(f"{a}*{b}={c.mul(a,b)}")
print(f"{a}/{b}={c.div(a,b)}")