age = int(input("Enter age: ")) 

if 0<=age<18:
    print("Underage")
elif 18<=age<60:
    print("Normal citizen")
else:
    print("Senior citizen")

print("Underage") if 0<=age<18 else print("Normal citizen") if 18<=age<60 else print("Senior citizen") 
# can i get the bonus now :) ???

day = int(input("Enter the day number")) 
print("Today is:", end=" ")

match day: #match is equivalent to switch statement of C++ in python
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

try:
    print(1/0)
except ZeroDivisionError:
    print("what u tryna do bro")
# when we don't know the type of error, we use
# except:
# except Exception as e:

finally:
    print("So u done?")
