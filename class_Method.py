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




harry = Employee("Harry", 455 ,"Instructor",9)
rohan = Employee("Rohan",45548,"Student",12)

harry.change_leaves(34)
rohan.change_leaves(54)

print('Leaves taken by Harry ',harry.no_of_leaves)
print('Leaves taken by Rohan ',rohan.no_of_leaves)