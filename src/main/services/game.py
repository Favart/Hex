from main.objects.squares import Squares
from main.objects.player import Player

class Game():
    
    def __init__(self,n):
        self.squares = Squares(n)
        self.first_player = Player(n)
        self.second_player = Player(n)
        self.turn = 1
        
    def display(self):
        print(self.first_player.squares + 2*self.second_player.squares)
        
    def play(self,square):
        self.squares.pull(square)
        if self.turn == 1:
            self.first_player.play(square)
            self.turn += 1
            print("Le joueur 1 a joué")
        else:
            self.second_player.play(square)
            self.turn -= 1
            print("Le joueur 2 a joué")
            
    def win(self):
        if self.first_player.win():
            print("Le joueur 1 a gagné")
            return 1
        elif self.second_player.win():
            print("Le joueur 2 a gagné")
            return 2