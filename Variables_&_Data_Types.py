name = "Md tanjid emam toha"
age =21
price =590400.271
old = False  
a= None 
b=4 
c= 3
print(type(name))
print(type(age))
print(type(price))
print(type(old))
print(type(a))
print(price-age)  #difference can be directly done no declaration is needed separately
print(price+age) 
""" in case of sum
it is also the same """
print(price*age)
print(price / age)
print(price%age) #remainder
print(b**c) #power

#Relational operators answer will be True or False

a = 2 
b = 5 
print (a==b) 
print (a!=b)  
print( a>b)
print(b>a)


#assignment operator
x=5
x=x+5
print(x)
x+=5
print(x)
#logical operators 
a=5
b=300.35
print (not False)
print (not(a<b))
print ((a>b)and(a< b))
print ((a>b)or (a< b))
c="2"
d=int(c) 
# Type conversion
print (a+b)  #auto cast example
print (b+d) # type cast example


name =input("Enter Your Name:")
age =int(input("AGE="))
cgpa=float(input("CGPA="))
print(name,age,cgpa)
print(type(name)) 
print(type(age)) 
print(type(cgpa))

first=int(input("enter first :"))
second=int (input("enter second:"))
side=float (input("enter side :"))
float1=float (input("enter float1 :"))
float2=float (input("enter float2 :"))
avarage=(float1+float2) /2


print("sum=",first+second)
print("area of square",side*side)
print("avarage :",avarage)

print(first>=second)