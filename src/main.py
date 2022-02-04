from main.objects.player import Player

player = Player(4)
player.play((0,0))
player.play((0,1))
player.play((0,2))
player.play((1,3))
print(player.squares)
print(player.win())