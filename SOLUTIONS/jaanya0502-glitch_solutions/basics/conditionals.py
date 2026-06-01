# correct if else ladder to check if person is underage, normal citizen or senior citizen
# [0,18) -> underage, [18,60) normal age, [60,inf) senior citizen
# bonus, can you reduce ladder to a one liner?
age = int(input("Enter age") )# ahh yes age is str , definitely

if age>= 0 and age<18:
    print("Lil bro")
elif age>= 18 and age<60:
    print("Pay up taxes, person")
else:
    print("U still good, unc?")

# one liner 
print("underage" if 0 <= age < 18 else "normal age" if 18 <= age < 60 else "senior citizen")

# complete the match

day = int (input("Enter the day number")) # dont forget to typecast to int

print("Today is: ",end="") # how can you avoid printing newline here?

if day == 1:
    print("Monday")
elif day == 2:
    print("Tuesday")
elif day == 3:
    print("Wednesday")
elif day == 4:
    print("Thursday")
elif day == 5:
    print("Friday")
elif day == 6:
    print("Saturday")
elif day == 7:
    print("Sunday")
else:
    print("Funday!")

# implement try catch

try:
    print(1/0)
except Exception  as exp: # ahh fix the syntax, also when u don't know the error what will u use?
    print("what u tryna do bro", exp)
    
finally:
    print("So u done?")






