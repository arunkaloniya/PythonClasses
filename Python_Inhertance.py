'''
Python Inheritance : 
Inheritance allows us to define a class that inherits all the methods and properties from another class.

Parent class is the class being inherited from, also called base class.

Child class is the class that inherits from another class, also called derived class.
'''

# Create a class named CARMA, with Description and Analyst properties, and a printname method:


class CARMA:
    def __init__(self,des,analyst) -> None:
        self.des=des
        self.analyst=analyst
    def printname(self):
        print(self.des,self.analyst)

abc=CARMA('CARMA',"Arun & Manish")

abc.printname()


# Creating a child class from CARMA let's say CARMAbaby

class CARMAbaby(CARMA):
    pass

abcBaby=CARMAbaby('CARMA Baby class','Arun & Manish')

abcBaby.printname()



'''
Add the __init__() Function
So far we have created a child class that inherits the properties and methods from its parent.
We want to add the __init__() function to the child class (instead of the pass keyword).
Note: The __init__() function is called automatically every time the class is being used to create a new object.


When you add the __init__() function, the child class will no longer inherit the parent's __init__() function.
Note: The child's __init__() function overrides the inheritance of the parent's __init__() function.
To keep the inheritance of the parent's __init__() function, add a call to the parent's __init__() function:


'''

class CARMAbaby2(CARMA):
    def __init__(self, des, analyst) -> None:
        self.des=des
        self.analyst=analyst
        return print(self.des,self.analyst)
        
abcBaby2=CARMAbaby2

abcBaby2("Baby owns init function"," Manish and Arun")



# To keep the parenet init definition call the parent init function to the child definition

class CARMAbaby2(CARMA):
    def __init__(self, des, analyst) -> None:
        CARMA.__init__(self, des,analyst)
        
        
abcBaby2=CARMAbaby2

abcBaby2("Baby owns init function"," Manish and Arun")














    
    
        