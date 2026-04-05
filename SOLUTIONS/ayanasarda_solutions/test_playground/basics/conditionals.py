# correct if else ladder to check if person is underage, normal citizen or senior citizen
# [0,18) -> underage, [18,60) normal age, [60,inf) senior citizen
# bonus, can you reduce ladder to a one liner?
age = int(input("Enter age")) # ahh yes age is str , definitely

if age < 18:
    print("underage")
elif (age>=18 and age<60):
    print("normal citizen")
else:
    print("senior citizen")

#one-liner
print("underage") if(age<18)else print("normal citizen")if(age>=18 and age<60) else print("senior citizen")

# complete the match

day = int(input("Enter the day number")) # dont forget to typecast to int

print("Today is: ",end='') # how can you avoid printing newline here?

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
    # fill in the rest
    case _:
        print("Funday !") 

# implement try catch

try:
    print(1/0)
except IndentationError: # ahh fix the syntax, also when u don't know the error what will u use?
    print("what u tryna do bro")
except ZeroDivisionError:
    print("zero error")
except Exception as e:
    print(f"error occured: {e}")
finally:
    print("So u done?")






