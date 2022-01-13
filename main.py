operation_done=input("please enter the operation to be done:").lower()
print("{}".format(operation_done))
if operation_done=="subtract" or operation_done=="divide":
    print(f"you chose {operation_done}")
    print("keep in mind the order matters")
number_1=float(input("enter your first number: "))
print(number_1)
number_2=float(input("enter your second number: "))
print(number_2)
if operation_done=="add":
    print("sum of the two numbers is: ",number_1+number_2)
elif operation_done=="subtract":
    print("the diffrence of the two numbers is: ",number_1-number_2)
elif operation_done=="multiply":
    print("the multiplication of the two numbers is ",number_1*number_2)
elif operation_done=="divide":
    print("the division of the two numbers is ",number_1/number_2)
else:
    print(f"syntax error {operation_done}")