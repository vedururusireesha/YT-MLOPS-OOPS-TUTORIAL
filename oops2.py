class employee:
    def __init__(self):
        self.id=123
        self.salary=50000
        self.designation="sde"
    #create method
    def travel(self,destination):
        print(f"employee is travelling to {destination}")


#create an object
sam=employee()
print(sam.id)
print(sam.salary)
print(sam.designation) 
sam.travel("hyderabad") 