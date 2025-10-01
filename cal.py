import datetime
num1=int(input("Enter the first number==>"))
op=input('Enter operator +,-,*,/,//===>')
num2=int(input("Enter the second number==>"))

if op=='+':
    print(num1+num2)
elif op=='-':
    print(num1-num2)
elif op=='*':
    print(num1*num2)
elif op=='/':
    print(num1/num2)
elif op=="%":
    print(num1%num2)
else:
    print("invalid operator")            




divide=f'{150/50}'
print(divide)


x=datetime.datetime.now()
print(x)

