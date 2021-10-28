
class PyCharm:
    def execute(self):
        print('Compiling')
        print('Running')

class Myeditor:
    def execute(self):
        print('Spell Check')
        print('Convention Check')
        print('Compiling')
        print('Running')

class laptop:

    def code(self,ide):
        ide.execute()

# ide = PyCharm()
ide = Myeditor()
lap1 = laptop()
lap1.code(ide)