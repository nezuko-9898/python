n1=int(input("Enter the number==>"))

facto = 1

if n1 < 0:
    print("Enter positive number")

elif n1 == 0:
    print(" The factorial 0 is 1")

else:
    for i in range(1,n1+1):
        facto *= i

print(f"The factorial {n1} is {facto}")
 