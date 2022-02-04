from PyInquirer import prompt
from main.views.abstract import AbstractView
from main.services.game import Game

class WelcomeView(AbstractView):

    def __init__(self):
        self.questions = [
            {
                'type': 'list',
                'name': 'choix_menu',
                'message': 'Que voulez-vous faire ?',
                'choices': ['1. Jouer :)']
            }
        ]
        self.size = [
            {
                'type': 'input',
                'name': 'size',
                'message': '. Sur quelle taille de plateau voulez-vous jouer ? (entier entre 3 et 11)'
            }
        ]

    @staticmethod
    def display_info():
        print('')

    def make_choice(self):
        reponse = prompt(self.questions)
        if reponse['choix_menu'] == '1. Jouer :)':
            size = prompt(self.size)
            AbstractView.session.game = Game(int(size['size']))
            from main.views.gaming import GamingView
            return GamingView()