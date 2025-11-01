# numbber = 10;
# print("init : " , numbber);
# print(f"init id : { id(numbber) }");
# numbber = 12;
# print("second : " , numbber);
# print("second : " , id(numbber));



# mutuable
setData = set();
# print("init : " , setData);
# print(f"init id : { id(setData) }");
# setData.add("jaydip");
# setData.add("ram");
# print("second : " , setData);
# print(f"second id : { id(setData) }");






# integer

a = 10
b=20
c= a// b
# print("result : " ,c);

c = a ** b

num = 1_0

print("result : " ,c);
print("number : " ,num);
print( type (num))



# booleans
isBoolean = True
count = 5
print(count+isBoolean) 
print(isBoolean) 
count = 0
print(bool(count))# zero is false otherwise everything is true


print("__________String______________________");

name = "jaydip jadhav"
print(name)
# slicing
print(name[::-1])
encoding = name.encode("utf-8");

print("encoding : " , encoding.decode("utf-8"));



# tuples
# tuple --> ()

print("_________________Tuples____________________")

data = ("jaydip" , 12 , "jadhav");
print("data : " , data[0])
(name, age , lastnaem , ) = data;
print(name ," : " , age , "  : " , lastnaem , " : ");
# membership testing
print("jaydip" in data);



# swapping numbers
a , b = 10 , 12
print(a         ,                b)

# swap
b , a = a , b;
print(a         ,                b);




# list
print("_________________List_____________________________")
students = ["jaydip" , "ram" , "aditya"]
students.append("jay")
students.sort()
students.pop(0);
classes = ["A ", "B"];
classes.extend(students);
print("claess : " , classes)
print(students);
# print(students[0]);



# set
unique_numbers = {1, 2, 3, 2, 1 , "jaydip"} 
unique_numbers.add(-100)
print(unique_numbers);
print(list(unique_numbers)[0]);


# dictionaries
stud = { "name": "jaydip" , "age" : 20};
studP = dict(name = "ram" , age =30);
print(studP);
print(stud)
print(stud["name"]);
print(stud.get("other" , "no value"));













   


