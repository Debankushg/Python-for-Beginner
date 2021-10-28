

class Employee:

    def __init__(self,name , salary, role,leaves):
        self.name = name
        self.salary = salary
        self.role = role
        self.leaves = leaves

harry = Employee("Harry", 455 ,"Instructor",9)

rohan = Employee("Rohan",45548,"Student",12)


print("Name is -", harry.name)
print("Salary is", harry.salary)
print("Role is ", harry.role)
print("leaves taken", harry.leaves)


print("Name is -", rohan.name)
print("Salary is", rohan.salary)
print("Role is ", rohan.role)
print("leaves taken",rohan.leaves)

