class Employee:
    no_of_leaves = 8

    def __init__(self,name , salary, role,leaves):
        self.name = name
        self.salary = salary
        self.role = role
        self.leaves = leaves

    def printdetails(self):
        return f"The Name is {self.name}. Salary is {self.salary}, and role is {self.role}"

    @classmethod
    def change_leaves(cls,newleaves):
        cls.no_of_leaves = newleaves


    @classmethod
    def from_dash(cls, string):
        return cls(*string.split("-"))


    @staticmethod
    def print_good(string):
        print("This is good " + string)

class programmer(Employee):
    def printprog(self):
        return f"The Name is {self.name}. Salary is {self.salary}, and role is {self.role}"



harry = Employee("Harry", 455 ,"Instructor",9)
rohan = Employee("Rohan",45548,"Student",12)

shubham = programmer("Shubham" , 555 , "Programmer")
karan = programmer("Karan" , 758 ,"programmer")


