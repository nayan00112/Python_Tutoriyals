# Polymorphism
# > Duck time
# > Operator Overloading
# > Method Overloading
# > Method Overriding

# Duck typing:

class Notepade:
    def execute(self):
        print("Typing")


class VS_CodeEditor:
    def execute(self):
        print("Run Compile Debug")


class MY_CodeEditor:
    def execute(self):
        print("Run Execute Compile Debug")


class Laptop:
    def code(self, ide):
        ide.execute()


ide = VS_CodeEditor()

l1 = Laptop()
l1.code(ide)  # Run Compile Debug

ide = Notepade()
l1.code(ide)  # Typing

ide = MY_CodeEditor()
l1.code(ide)  # Run Execute Compile Debug


# Here, ide has execute method (Becaus laptop call "execute" method) so whatever object of ide, it must have execute method.

# " This is ducktyping
#   If it looks like a duck
#     Swim like a duck
#   quacks like a duck
#  Then it probabaly is a duck."
