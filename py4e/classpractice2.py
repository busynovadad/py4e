class PartyAnimal:
    x = 0
    name = ""

    def __init__(self, z):
        self.name = z
        print('i am constructed 2', self.x, self.name)

    # def __init__(self):
    #     print('i am constructed 1', self.x, self.name)

    def party(self):
        self.x = self.x + 1
        print('so far', self.x, self.name)

    def __del__(self):
        print('i am destructed', self.x, self.name)


# test base constructor
an = PartyAnimal('test')
an.party()
# an = 43
an.party()
an = 42
print('an contains', an)
# print('an contains', an)

# test overloaded constructor
s = PartyAnimal('sally')
s.party()
s.party()
s = 42
print('s contains', s)

