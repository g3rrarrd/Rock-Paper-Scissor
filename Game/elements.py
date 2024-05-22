import random as r

class elements:
     
    def __init__(self):
        self.__elements = ["Paper", "Rock", "Scissor"]

    def element(self):
        number = r.randint(0,2)
        return self.__elements[number]
        