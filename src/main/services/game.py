from main.objects.squares import Squares
from main.objects.player import Player
from main.tools.tools_pygame import draw_blue, draw_red

class Game():
    
    def __init__(self,n):
        self.squares = Squares(n)
        self.first_player = Player(n,1)
        self.second_player = Player(n,2)
        self.turn = 1
        
    def clear(self):
        n = self.squares.get_shape()
        self.squares = Squares(n)
        self.first_player = Player(n,1)
        self.second_player = Player(n,2)
        self.turn = 1
        
    def state(self):
        return(self.first_player.squares+2*self.second_player.squares)
        
    def display_board(self):
        print(self.first_player.squares+2*self.second_player.squares)
        
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
        else:
            self.second_player.play(square)
            self.turn -= 1
            
    def win(self):
        if self.first_player.win():
            return 1
        elif self.second_player.win():
            return -1
        else:
            return 0
        
    def start_game_pvp(self):
        winner = self.win()
        while winner == 0:
            self.display_board()
            self.display_turn()
            row = int(input("Sur quelle ligne voulez vous jouer ? :"))
            column = int(input("Sur quelle colonne voulez vous jouer ? :"))
            self.play((row,column))
            winner = self.win()
        return winner