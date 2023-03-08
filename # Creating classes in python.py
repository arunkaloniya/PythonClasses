# Creating classes in python

class carma:
    a=10 # This is a property within class


#crating a object from a python class

obj1=carma()

obj1.a

'''
All classes have a function called __init__(), which is always executed
 when the class is being initiated.
Use the __init__() function to assign values to object properties, 
or other operations that are necessary to do when the object 
is being created:

'''
# Class __init__ with out parameters
class CarmaWithInit:
    def __init__(self):
        self.project=''' This project integrates the various Cards platforms'''
        self.analyst=['Manish','Arun']

        

obj2=CarmaWithInit()
obj2.analyst
obj2.project

# Class __init__ with some parameters

class CarmaWithInit:
    def __init__(self,project,analyst):
        self.project=project
        self.analyst=list(analyst.split(","))

        

obj2=CarmaWithInit(project='CARMA',analyst="Manish,Arun")
obj2.analyst
obj2.project



# __str__ representation within class

class CarmaWithStr:
    def __init__(self) -> None:
        self.project='CARMA'
        self.analyst='Manish,Arun'
    
    def __str__(self):
        return f"CARMA with Str function project {self.project} and analyst {self.analyst}"
    


obj3=CarmaWithStr()
obj3.analyst
obj3.project
print(obj3)
