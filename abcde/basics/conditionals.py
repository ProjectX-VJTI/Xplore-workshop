# correct if else ladder to check if person is underage, normal citizen or senior citizen
# [0,18) -> underage, [18,60) normal age, [60,inf) senior citizen
# bonus, can you reduce ladder to a one liner?
age = input("Enter age") # ahh yes age is str , definitely

if age <= 0:
    print("Lil bro")
elif age > 100:
    print("Pay up taxes, person")
else:
    print("U still good, unc?")


# complete the match

day = input("Enter the day number") # dont forget to typecast to int

print("Today is: ") # how can you avoid printing newline here?

match day:
    case 1:
        print("Monday")
    # fill in the rest
    case _:
        print("Funday !") 

# implement try catch

try:
    print(1/0)
except IndentationError: # ahh fix the syntax, also when u don't know the error what will u use?
    print("what u tryna do bro")
finally:
    print("So u done?")






