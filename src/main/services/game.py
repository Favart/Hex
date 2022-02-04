from main.objects.squares import Squares
from main.objects.player import Player

class Game():
    
    def __init__(self,n):
        self.squares = Squares(n)
        self.first_player = Player(n)
        self.second_player = Player(n)
        self.turn = 1
        
    def display_board(self):
        print(self.first_player.squares + 2*self.second_player.squares)
        
    def display_turn(self):
        if self.turn == 1:
            print("C'est au joueur 1 de jouer !")
        else:
            print("C'est au joueur 2 de jouer !")
        
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
            return 1
        elif self.second_player.win():
            return 2
        else:
            return 0
        
    def start_game(self):
        winner = self.win()
        while winner == 0:
            self.display_board()
            self.display_turn()
            row = int(input("Sur quelle ligne voulez vous jouer ? :"))
            column = int(input("Sur quelle colonne voulez vous jouer ? :"))
            self.play((row,column))
            winner = self.win()
        if winner == 1:
            print("Félicitations, le joueur 1 a gagné !")
        else:
            print("Félicitations, le joueur 2 a gagné !")
        return winner