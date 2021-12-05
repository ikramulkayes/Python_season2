class magical:
    def __init__(self):
        self.name1 = "werewolf"
        self.__name2 = "unicorn"
    def display(self):
        return self.__name2
creature = magical()
print(creature.name1)


class cuisine:
    def __init__(self):
        self.menu1 = "French"
        self.__menu2 = "Italian"

    def get(self):
        return self.__menu2
obj = cuisine()
obj.menu1 = "Turkish"
print(obj.menu1)