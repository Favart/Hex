from PyInquirer import prompt
from views.abstract import AbstractView
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

    @staticmethod
    def display_info():
        print('')

    def make_choice(self):

        reponse = prompt(self.questions)
        if reponse['choix_menu'] == '1. Jouer :)':
            n = input("Sur quelle taille de plateau voulez-vous jouer ? (entier entre 3 et 11)")
            AbstractView.session.game = Game(n)
            from views.gaming import GamingView
            return GamingView()