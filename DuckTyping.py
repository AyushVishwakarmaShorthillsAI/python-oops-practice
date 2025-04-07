# one thing behaing in different ways => Polymorphism

# Duck Typing : If it behaves like duck, then its a duck, no matching with looks
# It needs not to look like Duck, But behaves like Duck

class MyCharm:
    def execute(self):
        print('compiling')
        print('Running')

class MyEditor:
    def execute(self):
        print("Debug")
        print("Errors Check")
        print("compile")
        print('Runnig')

class laptop:
    def code(self, ide):
        ide.execute()

ide = MyEditor()

lap1=laptop()

lap1.code(MyCharm())
lap1.code(ide)

# How polymorphism ?
# Since we can use any ide(class) that has an execute fucntion, it will work 
# ide -> can be anything with an execute function in it => polymorphismS