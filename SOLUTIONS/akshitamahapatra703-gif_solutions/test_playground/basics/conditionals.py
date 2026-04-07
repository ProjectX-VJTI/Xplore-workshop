# correct if else ladder to check if person is underage, normal citizen or senior citizen
# [0,18) -> underage, [18,60) normal age, [60,inf) senior citizen
# bonus, can you reduce ladder to a one liner?
age = int(input("Enter age: ")) # Typecasting to int

# The Ladder
if age < 18:
    print("underage")
elif 18 <= age < 60:
    print("normal citizen")
else:
    print("senior citizen")

# One-liner Bonus
print("underage" if age < 18 else "normal citizen" if age < 60 else "senior citizen")


# complete the match

day = int(input("Enter the day number (1-7): "))

print("Today is: ", end="") 

match day:
    case 1: print("Monday")
    case 2: print("Tuesday")
    case 3: print("Wednesday")
    case 4: print("Thursday")
    case 5: print("Friday")
    case 6: print("Saturday")
    case 7: print("Sunday")
    case _: print("Funday !")

# implement try catch

try:
    print(1/0)
except ZeroDivisionError: 
    print("what u tryna do bro (can't divide by zero)")
except Exception as e: # This catches anything else
    print(f"An unexpected error occurred: {e}")
finally:
    print("So u done?")






