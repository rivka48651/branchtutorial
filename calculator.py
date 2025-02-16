





#!/usr/bin/python3
# Program make a simple calculator that can add, subtract, multiply and divide using functions


# This function multiplies two numbers
def multiply(x, y):
   return x * y

# This function divides two numbers
def divide(x, y):
   return x / y

=======
# פונקציות לכל פעולה
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    else:
        return x / y

# הצגת אפשרויות למשתמש

print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")


# Take input from the user 
choice = input("Enter choice(1/2/3/4):")
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if choice == '3':
   print("Not implemented yet")

elif choice == '4':
   print(num1,"/",num2,"=", divide(num1,num2))
else:
   print("Invalid input ",choice)
=======
# קבלת קלט מהמשתמש
choice = input("Enter choice(1/2/3/4): ").strip()  # .strip() מסיר רווחים נוספים

# בדיקה שהקלט הוא מספר תקין
if choice in ['1', '2', '3', '4']:
    # קבלת מספרים מהמשתמש
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    
    # ביצוע הפעולה בהתאם לבחירת המשתמש
    if choice == '1':
        print(f"{num1} + {num2} = {add(num1, num2)}")
    elif choice == '2':
        print(f"{num1} - {num2} = {subtract(num1, num2)}")
    elif choice == '3':
        print(f"{num1} * {num2} = {multiply(num1, num2)}")
    elif choice == '4':
        print(f"{num1} / {num2} = {divide(num1, num2)}")
else:
    print("Invalid input!")
>>>>>>> master
