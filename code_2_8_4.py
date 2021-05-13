class Human:
    def eat_spaghetti(self):
        print('Я могу есть спагетти')


class Robot:
    def drink_oil(self):
        print('Я могу потреблять машинное масло')


class Cyborg(Human, Robot):
    pass

cyborg_1 = Cyborg()
cyborg_1.eat_spaghetti()
cyborg_1.drink_oil()
