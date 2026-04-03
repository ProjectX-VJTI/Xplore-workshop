# correct if else ladder to check if person is underage, normal citizen or senior citizen
# [0,18) -> underage, [18,60) normal age, [60,inf) senior citizen
# bonus, can you reduce ladder to a one liner?
age =int(input("Enter age: ")) # ahh yes age is str , definitely

if age < 0:
    print("Still in joe mama's womb")
elif age < 18:
    print("Underage")
elif age < 60:
    print("Normal age")
else:
    print("Senior citizen")


# complete the match

day = int(input("Enter the day number: ")) # dont forget to typecast to int

print("Today is: ", end="") # how can you avoid printing newline here?

match day:
    case 1:
        print("Monday")# fill in the rest
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
finally:
    print("So u done?")

# Fix : In general exception for any error

try:
    print(1/0)
except Exception: 
    print("what u tryna do bro")  
finally:
    print("So u done?")

