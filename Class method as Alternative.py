class Employee:
    no_of_leaves = 8

    def __init__(self,name , salary, role):
        self.name = name
        self.salary = salary
        self.role = role
        


    @classmethod
    def change_leaves(cls,newleaves):
        cls.no_of_leaves = newleaves

    @classmethod
    def from_dash(cls,string):
        # params = string.split("-")
        # print(params)
        # return cls(params[0],params[1],params[2])
        return cls(*string.split("-"))



# harry = Employee("Harry", 455 ,"Instructor",9)
rohan = Employee.from_dash("Rohan-45548-instructor")
karan = Employee.from_dash("karan-480-student")

print("My name is ",karan.name)
print("Salary is",karan.salary)
print("my role is ",karan.role)
print("Leaves taken",karan.no_of_leaves)
print("*************************************************************************************************")
print("My name is ",rohan.name)
print("Salary is",rohan.salary)
print("my role is ",rohan.role)
print("Leaves taken",rohan.no_of_leaves)

