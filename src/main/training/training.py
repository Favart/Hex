import random
from main.tools.tools_training.initialise_Q_table import initialise_Q_table
from main.tools.tools_training.get_template import get_template
from main.services.game import Game

class Q_learning():
    
    def __init__(self,n,alpha=0.1,gamma=1,epsilon=0.2,Q=None):
        # Q_table initialisation
        if Q:
            self.Q_table = Q
        else:
            self.Q_table = initialise_Q_table(n)
        # Hyperparameters
        self.alpha = alpha
        self.gamma = gamma
        self.epsilon = epsilon
        # For plotting metrics
        self.all_epochs = []
        self.all_penalties = []
        # Game initialisation
        self.game = Game(n)
        
    def start(self,epochs):
        for i in range(epochs):
            self.game.clear()
            state = str(self.game.state())

            while self.game.win() == 0:
                if random.uniform(0, 1) < self.epsilon:
                    # Explore action space
                    action = random.choice(self.game.squares.get_last())
                else:
                    # Exploit learned values
                    action = max(self.Q_table[state], key=self.Q_table[state].get)
                    
                self.game.play(action)
                next_state = str(self.game.state())
                reward = 10*self.game.win()
                
                if reward == 0:
                    template = get_template(self.game.squares.get_last())
                    self.Q_table[next_state] = self.Q_table.setdefault(next_state, template)
                    
                    old_value = self.Q_table[state][action]
                    best_next = max(self.Q_table[next_state], key=self.Q_table[next_state].get)
                    next_max = self.Q_table[next_state][best_next]
                    
                    new_value = (1-self.alpha)*old_value+self.alpha*(reward-self.gamma*next_max)
                    self.Q_table[state][action] = new_value
                
                    state = next_state
                    
                else:
                    self.Q_table[state][action] = new_value
                
            print(" ----------------- \n -----------------")
                
            if i % 10 == 0:
                print(f"Episode: {i}")
                
        print("Training finished.\n")