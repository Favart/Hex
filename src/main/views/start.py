from PyInquirer import Separator, prompt
from views.abstract import AbstractView

class StartView(AbstractView):

    def __init__(self):
        self.questions = [
            {
                'type': 'list',
                'name': 'choix',
                'message': 'Hex Game !',
                'choices': ['. Entrer !']
            }
        ]

    def display_info(self):
        with open('assets/banner.txt', 'r', encoding="utf-8") as asset:
            print(asset.read())

    def make_choice(self):
        reponse = prompt(self.questions)
        if reponse['choix'] == '. Entrer !':
            from views.welcome import WelcomeView
            return WelcomeView()
