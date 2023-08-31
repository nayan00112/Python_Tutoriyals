from multipledispatch import dispatch


class A:

    @dispatch(int, int, int)
    def display(a, b, c):
        print("all int", a, b, c)

    @dispatch(float, int, str)
    def display(a, b, c):
        print("float int str", a, b, c)

    @dispatch(str, str, bool)
    def display(a, b, c):
        print("str str bool", a, b, c)


a1 = A()
a1.display(4, 6, 8)
a1.display("g", "e", True)
a1.display(7.55, 6, "h")


# Output:
# all int 4 6 8
# str str bool g e True
# float int str 7.55 6 h
