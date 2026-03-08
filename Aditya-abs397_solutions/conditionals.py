# correct if else ladder to check if person is underage, normal citizen or senior citizen
# [0,18) -> underage, [18,60) normal age, [60,inf) senior citizen
# bonus, can you reduce ladder to a one liner?
age = int(input("Enter age : ")) # ahh yes age is str , definitely

if age < 18:
    print("Lil bro")
elif age <= 60:
    print("Pay up taxes, person")
else:
    print("U still good, unc?")


    #BONUS
print("Lil Bro u are coming to island ;}" if age<18  else "Forgot the files already" if age <= 60 else "just count ur sins")

# complete the match
print("The week indexing is like 1 stands for monday and 7 for sunday")
day = int(input("Enter the day number : ")) # dont forget to typecast to int

print("Today is: ", end="") # how can you avoid printing newline here?

match day:
    case 1:
        print("Monday")
    # fill in the rest
    case _:
        print("Funday !")

# implement try catch

try:
    print(1/0)
except ZeroDivisionError: # ahh fix the syntax, also when u don't know the error what will u use?
    print("lmao what do u are? Newton")
finally:
    print("So u done? just check ur deeds")
