a=int(input("Enter number 1:"))
b=int(input("Enter number 2: ")) # result of input is "str"
sum=a+b
print(f"Sum of {a} and {b} is: {sum}")

# program to print square area
side=float(input("Enter side of square: "))
area=side**2
print(f"The Area of Square of side {side} is: {area:.2f}") # {area:.2f} limit ans to 2 decimal places

# check a>b
c=12
d=5
print((c>=d))