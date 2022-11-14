class A:
    def __init__(self, bb):
        self.b = bb
        print("A ", self.b)
        print("Constructor A")

    def __del__(self):
        print("destructed A")    


class B:
    def __init__(self):
        self.a = A(self)
        print("B ",self)
        print("constructor B")

    def __del__(self):
        print("destructed B")


def fun():
    b = B()

fun()
        