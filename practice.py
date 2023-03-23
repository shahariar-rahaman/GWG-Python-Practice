"""
#Hello World Python
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

#Logical Operators
print(5>1 and 5<10)#and Showed True if all condition return true.
print(5>1 and 5>10)#Here showed false.Because both condition do not return true.
print(5>1 or 5<10)#and Showed True if at least one condition return true.
print(5>1 or 5>10)#Here showed True.One condition do return true.
print(not 5>1 and 5<10)#not make True to False and False to True.

#if,else,elif statement
from_user = int(input("Input a Number: "))
if(from_user <= 10):
    print("From if Block")
elif(from_user <= 20):
    print("From elif Block")
else:
    print("From else Block")
"""

