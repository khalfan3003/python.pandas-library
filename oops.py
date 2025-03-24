class khalfan:
    pass


    #objects



class students:
    def __init__(self , name , age):
        self.name= name
        self.age = age

    def display(self):
        print("name:",self.name) 
        print("age : ",self.age)


obj1=students("john",23)
obj1.display()


