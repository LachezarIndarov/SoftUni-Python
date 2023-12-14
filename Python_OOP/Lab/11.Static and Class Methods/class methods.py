class Student:
    kind = "human"

    def __init__(self, name):
        self.name = name

    @classmethod
    def change_kind(cls):
        cls.kind = "asd"

s1 = Student("Test1")
s2 = Student("Test2")
print(s1.kind)
print(s2.kind)

s1.change_kind()
print(s1.kind)
print(s2.kind)