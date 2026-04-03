# correct if else ladder to check if person is underage, normal citizen or senior citizen
# [0,18) -> underage, [18,60) normal age, [60,inf) senior citizen
# bonus, can you reduce ladder to a one liner?
age = int(input("Enter age : ")) # ahh yes age is str , definitely

# if age <= 0:
#     print("Lil bro")
# elif age > 100:
#     print("Pay up taxes, person")
# else:
#     print("U still good, unc?")
if age>=0 and age<18:
    print("underage")
elif age>=18 and age<60:
    print("normal age")
elif age>=60:
    print("senior citizen")

#one liner
print("underage" if 0 <= age < 18 else "normal age" if 18 <= age < 60 else "senior citizen")



# complete the match

day = int(input("Enter the day number : ")) # dont forget to typecast to int

print("Today is: ",end="") # how can you avoid printing newline here?

match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")
    case 4:
        print("Thursday")
    # fill in the rest
    case _:
        print("Funday !") 

# implement try catch

try:
    print(1/0)
except Exception as exp: # ahh fix the syntax, also when u don't know the error what will u use?
    print("what u tryna do bro?",exp)
finally:
    print("So u done?")






