# correct if else ladder to check if person is underage, normal citizen or senior citizen
# [0,18) -> underage, [18,60) normal age, [60,inf) senior citizen
# bonus, can you reduce ladder to a one liner?
age = int(input("Enter age: ")) # ahh yes age is str , definitely
if age <= 0:
    print("You sure you wanna do this?")
elif age > 100:
    print("What?")
elif 0<age<18:
    print("Minor. ")
elif age>=18 and age<60:
    print("Adult. ")
elif age>=60: 
    print('Senior Citizen')


# complete the match

day = int(input("Enter the day number: ")) # dont forget to typecast to int
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
    case 1:
        print("Saturday")
    case 1:
        print("Sunday")
    # fill in the rest
    case _:
        print("Funday!") 

# implement try catch

try:
    print(1/0)
except Exception as error: # ahh fix the syntax, also when u don't know the error what will u use?
    print("what u tryna do bro", error)
finally:
    print("So u done?")