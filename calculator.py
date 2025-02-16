





#!/usr/bin/python3
# Program make a simple calculator that can add, subtract, multiply and divide using functions

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
