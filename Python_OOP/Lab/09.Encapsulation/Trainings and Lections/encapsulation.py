class Student:
    def __init__(self, number, id_number):
        self.number = number
        self.__id_number = id_number
        self._grades = [5, 6]

    def calculate_age(self):
        year = self.__id_number[:2]
        # age = datetime.now() - year

    def get_id_number(self):
        return self.__id_number[:6]


student = Student("1234a", "2001010101")
student._Student__id_number = "9001010101"
print(student._grades) # [5, 6]
print(student.get_id_number()) # 900101

#--------------------------------------------------------------------------------

class Student:
    def __init__(self, number, id_number):
        self.number = number
        self.__id_number = id_number
        self._grades = [5, 6]

    def calculate_age(self):
        year = self.__id_number[:2]
        # age = datetime.now() - year

    def get_id_number(self):
        return self.__id_number[:6]

    def set_id_number(self, val):
        if val[:2] != "90":
            raise ValueError("Only '90 students are accepted")
        self.__id_number = val



student = Student("1234a", "2001010101")
student._Student__id_number = "9001010101"
print(student.get_id_number()) # 900101
student.set_id_number("202014") # ValueError: Only '90 students are accepted

