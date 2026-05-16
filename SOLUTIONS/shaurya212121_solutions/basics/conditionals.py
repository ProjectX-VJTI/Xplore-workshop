# correct if else ladder to check if person is underage, normal citizen or senior citizen
# [0,18) -> underage, [18,60) normal age, [60,inf) senior citizen
# bonus, can you reduce ladder to a one liner?
age = int(input("Enter age: ")) # ahh yes age is str , definitely

# Main logic for age ranges
if age < 18:
    print("Underage")
elif age < 60:
    print("Normal citizen")
else:
    print("Senior citizen")

# Bonus one-liner (uncomment to test):
# print("Underage" if age < 18 else "Normal citizen" if age < 60 else "Senior citizen")

if age <= 0:
    print("Lil bro")
elif age > 100:
    print("Pay up taxes, person")
else:
    print("U still good, unc?")


# complete the match

day = int(input("Enter the day number: ")) # dont forget to typecast to int

print("Today is: ", end="") # how can you avoid printing newline here?

match day:
    case 1:
        print("Monday")
    # fill in the rest
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
        print("Funday !") 

# implement try catch

try:
    print(1/0)
except ZeroDivisionError: # ahh fix the syntax, also when u don't know the error what will u use?
    print("what u tryna do bro")
except Exception as e: # This is the catch-all you use when you don't know the exact error
    print(f"Unknown error caught: {e}")
finally:
    print("So u done?")