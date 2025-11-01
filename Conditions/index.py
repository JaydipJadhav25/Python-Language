age = input("enter you age : ")
print("age is : " , age)

# Convert the age string to an integer
age_as_int = int(age)

if age_as_int < 18:
    print("you are bachcha!");
elif age_as_int <= 0:
    print("data wrong age takl nit check kr !")
else:
    print("you are manus !")



salary = int(input("enter salary : "));

print(salary);


# one line 
print( 100 if salary > 100 else 300);




# match conditions
sit = input("enter sit type :").lower();

match sit:
    case "sleeper":
        print("no ac");
    case "luxiery":
        print("yes , avaliable ac");

    case _:
        print("invalidate");
