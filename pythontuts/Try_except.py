num1=int(input("Enter number one:"))
num2=int(input("Enter number two:"))
print(num1+num2)


num3=input("Enter number three:")
num4=input("Enter number Four:")
try:
    print(int(num3)+int(num4))
except Exception as e:
    print(e)

print("This line is very important")