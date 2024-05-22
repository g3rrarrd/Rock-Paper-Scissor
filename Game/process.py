class process:

    def __init__(self):
        self.__result = None
        self.__option = {0: "Lose", 1:"Win", 2:"Draw"}

    def case1(self):
        self.__result = 0

    def case2(self):
        self.__result = 1

    def case3(self):
         self.__result = 2

    def result(self, player, computer):

        cases = {0: self.case1, 1: self.case2, 2: self.case3}

        print("\nPlayer: %s  Computer: %s" % (player, computer))

        if((player == "Scissor" and computer == "Paper") or 
           (player == "Paper" and computer == "Rock") or 
           (player == "Rock" and computer == "Scissor")):
            cases.get(1)()
        elif((player == "Paper" and computer == "Scissor") or
             (player == "Scissor" and computer == "Rock") or
             (player == "Rock" and computer == "Paper")):
            cases.get(0)()
        else:
            cases.get(2)()
        return self.__result
    
    def print_result(self):
        print(self.__option.get(self.__result)+ "\n")