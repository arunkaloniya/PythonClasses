'''
This are mainly 5 types of the data types in python. 

lists
tuples
dictionaries
strings
sets

'''


#Lists
'''
List can contain different types of objects such as integer, float, string etc.
the pair of braces actually differentiate it from the datatypes

index of the list start from 0 to n-1 where n is number of items in the list

Syntax : list[start : stop : step]
start : refers to starting position.
stop : refers to end position.
step : refers to increment value.

x[-1] selects the last element from list.

x[:3] returns first three items
x[0:3] also returns first three items
x[::-1] reverses the whole list

'''

x = [142, 124, 234, 345, 465, 'A', 'C', 'E', 'M', 'AA', 44, 5.1, 'KK']
#ind=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

#to find out the index of the item in the list you can use index method of the list

ind=[]
for z in x:
    ind.append(x.index(z))

print(ind)

# By position

x[0] #first item
x[1] #second item


#sorted function to sort the list
#it only support the one type of the data .i.e either numeric or string , default is ascending order and to sort it in descending order supply reverse=False 

x=[1,3,2,5,8]
sorted(x)


x=['a','b','c']
sorted(x)

#in descending order
sorted(x,reverse=True)


# adding 5 in list items
x = [1, 2, 3, 4, 5]
for i in range(len(x)):
    x[i] = x[i] + 5  # this line can also be written like this x[i] += 5
print(x)


# join two lists using + operator
X = [1, 2, 3]
Y = [4, 5, 6,8]
Z = X + Y
print(Z)



import numpy as np
X = [1, 2, 3]
Y = [4, 5, 6]
Z = np.add(X, Y) # it would add only if size of both the list is same
print(Z)

#Multiplication
Z=np.multiply(X,Y)
Z

#Divide
Z=np.divide(X,Y)
Z
#Subtract
Z=np.subtract(X,Y)
Z


### TUPLE
'''
Tuple
Like list, tuple can also contain mixed data. But tuple cannot be mutable or changed once created whereas list can be mutable or modified.
Another difference is a tuple is created inside parentheses ( ). Whereas, list is created inside square brackets [ ]

Examples '''

mytuple = (123,223,323)
City = ('Delhi','Mumbai','Bangalore')



'''
Dictionary
It works like an address book wherein you can find an address of a person by searching the name. 
In this example. name of a person is considered as key and address as value. 
It is important to note that the key must be unique while values may not be.
 Keys should not be duplicate because if it is a duplicate, you cannot find exact values associated with key. 
 Keys can be of any data type such as strings, numbers, or tuples.


'''

my_dict={'Name':['Arun','Ankit','Shashi']
         ,'Age':[30,31,32]}

my_dict.keys()
my_dict.values()
my_dict.items()


keys = ['a', 'b', 'c']
values = [1, 2, 3]
d1 = dict(zip(keys, values))


####Sets
#Sets are unordered collections of simple objects. They are mainly used to check whether an object is present in the set and compute mathematical operations such as intersection, union, difference etc.


X = set(['A', 'B', 'C'])




























