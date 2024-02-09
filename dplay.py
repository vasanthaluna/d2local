class dplay():
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def gt_data(self):
        self.name=input("enter a name:")
        self.age=int(input("enter your age:"))
    
    def display(self):
        print("name of person:")
        print("age:")
