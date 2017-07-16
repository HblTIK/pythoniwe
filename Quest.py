import random
import sys

greetings = ["'Ты не пройдешь!'\n", "'...'\n", "'Опа на!'\n"]
positive_reactions = ["Ну ладно, вали.\n",
                      "Только не бей!\n"
                      ]
negative_reactions = ["Я тут ем вообще-то, подожди немного.\n",
                      "Иди нахер.\n",
                      "Ты думаешь это на меня сработает?'\n",
                      "Чо ты о себе возомнил?\n"
                      "..."
                      ]
MOODS = ('плохое', 'нормальное', 'хорошее')
RANKS = ('малого', 'среднего', 'высокого')
ACTIONS = '[A]Флиртовать, [B]Подкупить, [E]Умолять, [P]Испугать, [T]Угрожать: \n'


class Bureaucrat:
    '''A government employee who works in the Institution.'''

    def __init__(self):
        self.rank = random.choice(RANKS)
        self.mood = random.choice(MOODS)
        self.negative = False

    def greet(self):
        '''A random greeting from the government employee.'''

        print(random.choice(greetings))
        print('Перед вами Жаба {} роста.'.format(self.rank))
        print('Похоже её настроение {}.'.format(self.mood))

    def react_positively(self):
        '''A positive reaction to the choice of the player.'''

        self.negative = False
        print(random.choice(positive_reactions))

    def react_negatively(self):
        '''A negative reaction to the choice of the player.'''

        self.negative = True
        print(random.choice(negative_reactions))

    def act(self):
        self.action = input("Что вы будешь делать? {} ".format(ACTIONS))
        if self.action == 'Q':
            print('Пройдено (нет).')
            sys.exit()
        elif self.action == 'W':
            self.negative = False
        else:
            self.react()

    def react(self):
        '''A reaction to the choice of the player.'''

        if self.mood == 'хорошее' and self.rank == 'малого':
            if self.action == "A":
                self.react_positively()
            else:
                self.react_negatively()
        elif self.mood == 'хорошее' and self.rank == 'среднего':
            if self.action == "B":
                self.react_positively()
            else:
                self.react_negatively()
        elif self.mood == 'хорошее' and self.rank == 'высокого':
            if self.action == "T":
                self.react_positively()
            else:
                self.react_negatively()
        elif self.mood == 'нормальное' and self.rank == 'высокого':
            if self.action == "E":
                self.react_positively()
            else:
                self.react_negatively()
        elif self.mood == 'нормальное' and self.rank == 'малого':
            if self.action == "P":
                self.react_positively()
            else:
                self.react_negatively()
        elif self.mood == 'плохое' and self.rank == 'малого':
            if self.action == "T":
                self.react_positively()
            else:
                self.react_negatively()
        elif self.mood == 'плохое' and self.rank == 'среднего':
            if self.action == "A":
                self.react_positively()
            else:
                self.react_negatively()
        elif self.mood == 'плохое' and self.rank == 'высокого':
            if self.action == "P":
                self.react_positively()
            else:
                self.react_negatively()
        elif self.mood == 'нормальное' and self.rank == 'среднего':
            if self.action == "P":
                self.react_positively()
            else:
                self.react_negatively()


print('Вам нужно пробежать 40 этажей с Жабами(зачем?)\n')
bureaucrat = Bureaucrat()
bureaucrat.greet()
while True:
    bureaucrat.act()
    if bureaucrat.negative is False:
        bureaucrat = Bureaucrat()
        bureaucrat.greet()