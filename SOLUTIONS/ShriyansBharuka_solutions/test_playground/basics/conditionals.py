# correct if else ladder to check if person is underage, normal citizen or senior citizen
# [0,18) -> underage, [18,60) normal age, [60,inf) senior citizen
# bonus, can you reduce ladder to a one liner?
age = int(input("Enter age ")) # ahh yes age is str , definitely

if age < 18 and age > 0:
    print("Lil bro")
elif age >= 18 and age <60:
    print("Pay up taxes, person")
else:
    print("U still good, unc?")
# we can use ternary operator to reduce the ladder into one line 
print("LIl bro " if 0<age<18 else "Pay up taxes person " if age <60 else "U still good unc ?" )

# complete the match

day = int(input("Enter the day number")) # dont forget to typecast to int

print("Today is: ", end="") # how can you avoid printing newline here?

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
        print("Funday !") 

# implement try catch

try:
    print(1/0)
except ZeroDivisionError: # ahh fix the syntax, also when u don't know the error what will u use?
    print("what u tryna do bro")
finally:
    print("So u done?")

try:
    print(1/0)
except Exception as e:
    print(f"Error: {e}")
finally:
    print("So u done?")


#done
