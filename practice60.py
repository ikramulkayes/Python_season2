class sports:
    def __init__(self):
        self.name1 = "football"
        self.__name2 = "cricket"
    def display(self):
        return self.__name2
obj = sports()
print(obj.__name2)