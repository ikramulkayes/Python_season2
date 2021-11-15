class Joker:
    def __init__(self,name,power,is_he_psycho):
        self.name = name
        self.power = power
        self.is_he_psycho = is_he_psycho





j1 = Joker('Heath Ledger', 'Mind Game', False)
print(j1.name)
print(j1.power)
print(j1.is_he_psycho)
print("=====================")
j2 = Joker('Joaquin Phoenix', 'Laughing out Loud', True)
print(j2.name)
print(j2.power)
print(j2.is_he_psycho)
print("=====================")
if j1 == j2:
    print('same')
else:
    print('different')
j2.name = 'Heath Ledger'
if j1.name == j2.name:
    print('same')
else:
    print('different')
#Write your code for 2,3 here

#subtask 2
print("j1 and j2 are different objects and their memory locations are different.")

#subtask 3
print("j1 and j2 are different objects but the name property of them are same. This is why the if statement is showing same in the output.")
