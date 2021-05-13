class School:
    def wear_uniform(self):
        print('В школе все должны носить форму')


class University:
    def wear_uniform(self):
        print('Можно носить любую одежду, если ты студент')

school_1 = School()
university_1 = University()

list_1 = [school_1, university_1]
for instances in list_1:
    instances.wear_uniform()
