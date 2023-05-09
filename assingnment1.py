# 1.

name="Vinay Kumar"         #string variable
inform=["vinay",63,3.2,1+4j,True]   #list 
pi=3.14                           #float variable
tupl=(1,"Ram",2.45,True,2+4j)     #tuple


#2.
 
var1=''                             #string
var2='[DS,ML,Python]'               #string
var3=['DS', 'ML','Python']          #List
var4=1.                             #float

#Solution:
print(type(var1), type(var2), type(var3), type(var4))


#3.

#Ans- 3. 1. / operator is used to divide two numbers
a=20
b=5
print(a/b)                       #4


#Ans-3.2. % (modulo) operator is used to find remainder of the two numbers.
  
c=a%b                           #0

#Ans-3.3. // operator is used to find the floor division of the two no.
n1=15
n2=2
fd = n1 // n2
print(fd)                            #7

#Ans-3.4  ** operator is used to find exponent

exp=n1**n2
print(exp)                            #225


#4

info=["vinay",67,84.5,1+4j,True,False,'Sudhanshu Sir','Urvi mam','Vishwa Sir','Krish Sir'] 
for i in info :
  print(str(i) + " " + str(type(i)))
  
#5

A=24
B=3
while B<=A:
  if A%B==0:
    print("A is purely divisible by B. ")
    C=A/B 
    print(str(A), "is divisible " + str(C) + " TIMES by "+str(B))
    break;
  else :
    print('A is not divisible by B')

#6. 

l=list(range(1,26))
print(l)
for i in l:
  if i%3==0:
    print(i," is divisible by 3")
  else:
    print(i," is not divisible by 3")

#7. 
# Mutable data types allow to change  its values via indexing 
#Example : List, Set, Dictionary
# Immutable data types does not allow us to change its values.
#Example : tuples,int, float, bool


   