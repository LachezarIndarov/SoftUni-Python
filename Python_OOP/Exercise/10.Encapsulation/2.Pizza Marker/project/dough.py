class Dough:
    def __init__(self, flour_type: str, baking_technique: str, weight: float):
        self.flour_type = flour_type
        self.baking_technique = baking_technique
        self.weight = weight

    @property
    def flour_type(self):
        return self.__flour_type

    @flour_type.setter
    def flour_type(self, flour_type):
        if flour_type == "":
            raise ValueError("The flour type cannot be an empty string")
        else:
            self.__flour_type = flour_type

    @property
    def baking_technique(self):
        return self.__baking_technique

    @baking_technique.setter
    def baking_technique(self, baking_technique):
        if baking_technique == "":
            raise ValueError("The baking technique cannot be an empty string")
        else:
            self.__baking_technique = baking_technique

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, weight):
        if weight <= 0:
            raise ValueError("The weight cannot be less or equal to zero")
        else:
            self.__weight = weight
