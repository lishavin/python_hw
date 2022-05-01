import math

#1
num1= int(input('Number1: '))
num2= int(input('Number2: '))
a,b = divmod(num1,num2)

print('몫:', a)
print('나머지:', b)

#2
x= int(input('Enter a value for x: '))

func= 3*x**5 + 2*x**4 + - 5*x**3 - x**2 + 7*x - 6
print('Polynomial for x =', x, ':', func)

#3
n= int(input('Enter the number of people: '))
p= 1-math.factorial(365)/((365**n)*math.factorial(365-n))
    
print('Probability:', 100*p)
