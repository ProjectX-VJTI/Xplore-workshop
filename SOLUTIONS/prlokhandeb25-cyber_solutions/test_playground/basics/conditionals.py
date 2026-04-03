# correct if else ladder to check if person is underage, normal citizen or senior citizen
# [0,18) -> underage, [18,60) normal age, [60,inf) senior citizen
# bonus, can you reduce ladder to a one liner?
age = int(input("Enter age ")) # ahh yes age is str , definitely
 
if age <= 18:
    print("Underage")
elif age > 18 & age < 60:
    print("Normal age")
else:
    print("Senior citizen")


day = int(input("Enter the day number: "))

print("Today is: ", end="")

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
else:
    print("Funday!") 
# version is not up to date so using if elif
# implement try catch
try:
    print(1/0)
except Exception as e:
    print("what u tryna do bro")
finally:
    print("So u done?")






