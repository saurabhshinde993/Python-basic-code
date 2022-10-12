#websides 
'''
1) w3school.com
2) programiz
3) geeksforgeeks.com
4) javascript
5) coding bat
6) hakkerrank
7) leetcode
'''

# Operators
'''
operators is symbol that perform to certain operation
'''

#1) Arithmatic Operators 
print('arithmatic operators-------->')
x=10
y=3
print(x+y)    #addition.
print(x-y)    #substraction.
print(x*y)    #multiplication.
print(x/y)    #division.             #o/p division
print(x%y)    #modulo operater.      #o/p reminder
print(x//y)   #floor division.       #o/p number of division 
print(x**y)   #exponant division.     


#2) relation/comparison operator  # >,<,<=,>=,==,!=  #output of rlation operator is always logical

print('relation/comprason operator------------->')
a=4
b=3
print(a>b)
print(a<b)
print(a!=b)
print(a==b)
print(a<=b)
print(a>=b)


#3)Logical operator ---> and,or,not    #logical output always logical  i.e true or false 

'''
and-->if both argument are true then only the result is true 
or-->if atleast one orgument is true then result is true 
not-->complement of other 
'''
print('Logical operator------------->')
a=2
b=3
c=4
print(a<b and a<c)
print(a>b or a>c)
print(a>b or a<b)
print(not a>b)

#4) Idntify operator--->is,is not   #o/p always logical
print('identify operator------->')
a=10
b=20
print(a is b)
print(a is not b)

#5)Membership operator ---> in and not in 
print('membershipoperator----------->')
list=[1,2,3,4,4,5,5555]
print(5555 in list)
print(5555 not in list)


#6)assingment operator
print('assingment operator')
a=2
a+=4    #a=a+4
print(a)

a-=4
print(a)

a*=4
print(a)

a/=2
print(a)

a%=2
print(a)

b=2
b**=3
print(b)
