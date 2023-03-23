#Hello World Python
"""
print("Hello World!")

#Python list of loop
names = ["Shahariar","Arif","Ratul","Adnan"]
for name in names:
    print(name)
    
#range function
for x in range(10):
    print(x)
    
#type function
print(type(7))
print(type("S"))
print(type(0.7))

#implicit conversion 
print(7+8.5)
#explicit conversion
a = 10
b = "20"
print(a+int(b))

#In python string and interger or flot type data not allowed to merge.Here we need make explict operation.
a = 10
b = "Sting"
print(b +" "+ str(a))

#function: In python function return produce a value.And return is a statement.
def person(name,occupation):
    print("I am "+name)
    print("I am doing "+occupation)
person("Shahariar","Unemployed")

#function with return statement
def area_of_triange(base,height):
    return base*height/2
print(area_of_triange(12,24))

#len() function
print(len("Md. Shahariar Rahaman"))

#In python >,<,>=,<= in not work between float/integer vs string
print(1<"1")#showed error
print(1>"1")#showed error
print(1<="1")#showed error
print(1>="1")#showed error
   
The comparison operators include:
== (equality)
!= (not equal to)
> (greater than)
< (less than)
>= (greater than or equal to)
<= (less than or equal to)

#Unicode value
print("my computer" >= "my chair")#Showed true because both first letter unicode value same.
print("Brown" < "brown")#Showed True.Because capital letter B's unicode value 66 and short hand letter unicode value 98.So, 98 bigger than 66.Thats why here output True
"""