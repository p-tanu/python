a=10
b=20
c = a + b
print(c)


d = 12.4
f = 43.9
g = d+f
print(type(g))
print(g)

name = "pen"
print(type(name))

#snakecase 
is_valid_user = True
#because it looks like a snake

#camelCase
#IsValidUser = true 
#because it looks like a camel

#variable name cant have white spaces
#cant have special characters
#good to have lowercase
#avoid using built in keywords --> list ,int ,float
#variable names are case sensitive
#use snake caseing to define the variable

def sum():
    a1=10
    b1=20
    print(a1+b1)

print("hi")
sum()

#python is dynamically typed language whereas java is statically typed language
#in python we can change type of the variable any time in program
#we can use same named variable having different data types
#but in java it will give compilation error 


#calculate tax
income = 17000
tax_per = 0.2
tax = income * tax_per
print(tax)

#Strings ->ordered sequence of character
name = "sam"
first_name = 'sam'

print(name[-1])

#indexing 0 1 2       0 -2 -1 
#slicing

str_a = "abcdefg"
print(str_a[1:4])
print(str_a[:4])
print(str_a[2:])
print(str_a[0:7:2])
#to reverse
print(str_a[::-1])

last_name = "Patil"
print(last_name[::-1])


#string is immutable
name = "tie"
#name[1] = "o" #you cant do this
name1 = name[0] + "o" + name[2]
print(name1)






