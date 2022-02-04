from PyInquirer import prompt
from main.views.abstract import AbstractView

class GamingView(AbstractView):

    def __init__(self):
        self.questions = [
            {
                'type': 'list',
                'name': 'choix',
                'message': 'Voulez-vous rejouer ?',
                'choices': ['1. Oui :D',
                            '2. Non :/']
            }
        ]

    @staticmethod
    def display_info():
        print("La partie va commencer :)")

    def make_choice(self):
        AbstractView.session.game.start_game()
        reponse = prompt(self.questions)
        if reponse['choix'] == '1. Oui :D':
            from main.views.welcome import WelcomeView
            return WelcomeView()
        elif reponse['choix'] == '2. Non :/':
            pass