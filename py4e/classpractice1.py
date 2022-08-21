class PartyAnimal:
    x = 0

    def __init__(self):
        print('i am constructed', self.x)

    def party(self):
        self.x = self.x + 1
        print('so far', self.x)

    def __del__(self):
        print('i am destructed', self.x)


an = PartyAnimal()
an.party()
# an = 43
an.party()
an = 42
print('an contains', an)
# print('an contains', an)

