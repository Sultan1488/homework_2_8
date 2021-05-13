class VideoGame:
    def __init__(self, name, developers, main_character):
        self.name = name
        self.developers = developers
        self.main_character = main_character

    def info(self):
        print(f'Name: {self.name}\n'
              f'Developers: {self.developers}\n'
              f'Main character: {self.main_character}')

the_witcher = VideoGame('The Witcher', 'CD Project', 'Geralt of Rivia')
call_of_duty = VideoGame('Call of Duty', 'Activision', 'Capitan Price')
god_of_war = VideoGame('God of War', 'Santa Monica Studio', 'Kratos')
the_witcher.info()
call_of_duty.info()
god_of_war.info()
