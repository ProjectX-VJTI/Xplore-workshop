age = int(input("Enter age: "))

if age < 18:
    print("Underage")
elif age < 60:
    print("Normal citizen")
else:
    print("Senior citizen")

day = int(input("Enter the day number: "))

print("Today is: ", end="")

match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")
    case _:
        print("Invalid day")

try:
    print(1/0)
except Exception:
    print("An error occurred")
finally:
    print("Program finished")