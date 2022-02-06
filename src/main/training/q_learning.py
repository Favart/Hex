import random
import matplotlib.pyplot as plt
from main.tools.tools_training.initialise_Q_table import initialise_Q_table
from main.tools.tools_training.get_template import get_template
from main.services.game import Game

class Q_learning():
    
    def __init__(self,n,alpha=0.1,gamma=1,epsilon=0.8,Q=None):
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
                #if self.game.squares.get_last():
                #    self.game.play(random.choice(self.game.squares.get_last()))
                next_state = str(self.game.state())
                reward = 10*self.game.win()
                
                old_value = self.Q_table[state][action]
                
                if reward == 0:
                    template = get_template(self.game.squares.get_last())
                    self.Q_table[next_state] = self.Q_table.setdefault(next_state, template)
                    
                    if random.uniform(0, 1) < self.epsilon:
                        # Explore action space
                        best_next = random.choice(self.game.squares.get_last())
                    else:
                        # Exploit learned values
                        best_next = min(self.Q_table[next_state], key=self.Q_table[next_state].get)
                    next_max = self.Q_table[next_state][best_next]
                    self.game.play(best_next)
                    
                    new_value = (1-self.alpha)*old_value+self.alpha*(reward+self.gamma*next_max)
                    self.Q_table[state][action] = new_value
                    
                    state = next_state
                    
                    action = best_next
                    next_state = str(self.game.state())
                    reward = 10*self.game.win()
                    
                    old_value = self.Q_table[state][action]
                    
                    template = get_template(self.game.squares.get_last())
                    self.Q_table[next_state] = self.Q_table.setdefault(next_state, template)
                    
                    if random.uniform(0, 1) < self.epsilon:
                        # Explore action space
                        best_next = random.choice(self.game.squares.get_last())
                    else:
                        # Exploit learned values
                        best_next = max(self.Q_table[next_state], key=self.Q_table[next_state].get)
                    next_max = self.Q_table[next_state][best_next]
                    
                    new_value = (1-self.alpha)*old_value+self.alpha*(reward+self.gamma*next_max)
                    self.Q_table[state][action] = new_value
                    
                    state = next_state
                
                else:
                    self.Q_table[state][action] = (1-self.alpha)*old_value+self.alpha*reward
            
            self.all_epochs.append(i)
            self.all_penalties.append(((reward/10)+1)/2)
            
            if i % 10 == 0:
                print(" --------------- \n ---------------")
                print(f"Episode: {i}")
                
        print("Training finished.\n")
        
    def display(self):
        plt.plot(self.all_epochs,self.all_penalties)
        plt.show
        
    def test(self,epochs):
        wins = 0
        losts = 0
        for i in range(epochs):
            self.game.clear()
            while self.game.win() == 0:
                state = str(self.game.state())
                if state in self.Q_table:
                    action = max(self.Q_table[state], key=self.Q_table[state].get)
                else:
                    action = random.choice(self.game.squares.get_last())
                self.game.play(action)
                if self.game.win() == 0:
                    action = random.choice(self.game.squares.get_last())
                    self.game.play(action)
                if self.game.win() == 1:
                    wins += 1
                elif self.game.win() == -1:
                    losts += 1
        return wins,losts