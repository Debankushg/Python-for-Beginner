
class student:

    school = "Deban"

    def __init__(self,m1,m2,m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def avg(self):
        return (self.m1+self.m2+self.m3)/3

    # def get_m1(self):
    #     return self.m1
    #
    # def set_m1(self,value):
    #     self.m1 = value
    #

    @classmethod
    def getschool(cls):
        return cls.school

    @staticmethod
    def info():
        print("This is Student Class.... in ABC module")


s1 = student(34,67,32)
s2 = student(89,97,62)

print(s1.avg())
print(s2.avg())
print(student.getschool())
student.info()