class employee:
    def __init__(self):
        print("started executing attributes")
        self.id=123
        self.salary=50000
        self.designation="sde"
        print("attributes have been initiated")
    #create method
    def travel(self,destination):
        print("the method should be called manually")
        print(f"employee is travelling to {destination}")


#create an object
sam=employee()
#print(sam.id)
#print(sam.salary)
#print(sam.designation) 
#sam.travel("hyderabad") 