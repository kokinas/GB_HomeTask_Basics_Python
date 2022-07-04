class Clothes():
    spend_raw_common = []

    def __init__(self, name, size):
        self.name = name
        self.size = size
        self.spend_raw_common.append(self.spend_raw())

    @property
    def total_spend(self):
        return 'Total spend raw: %.2f' % sum(self.spend_raw_common)


class Suit(Clothes):

    def spend_raw(self):
        return 2 * self.size + 0.3


class Coat(Clothes):

    def spend_raw(self):
        return round(self.size / 6.5 + 0.5, 2)


suit_1 = Suit('suit_bx9', 28)
suit_2 = Suit('suit_ie2', 19)
suit_3 = Suit('suit_xe2', 25)
print(suit_3.total_spend)
suit_4 = Suit('suit_a22', 15)
suit_5 = Suit('suit_ee2', 27)
coat_1 = Coat('coat_oc2', 30)
coat_2 = Coat('coat_os2', 19)
coat_3 = Coat('coat_ac2', 22)
coat_4 = Coat('coat_bc2', 17)

print(suit_1.name, suit_1.spend_raw())
print(coat_1.name, coat_1.spend_raw())
print(coat_2.name, coat_2.spend_raw())
print(suit_5.spend_raw())
print(coat_4.total_spend)
print(Coat.__bases__)
